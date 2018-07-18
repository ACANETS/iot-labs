#!/usr/bin/env python

"""Create a JACK client that analyzes audio stream input 

(c) Yan Luo. 2018-present. All rights reserved. 

The client reads in audio blocks and uses aubio library (aubiotrack function)
to figure out the beats per minute (BPM). Then it will follow BPM to shine
the LEDs periodically to sync with the rhythm of the music.

This requires aubiotrack starts already and jackd server running.

EITHER
capture_1 -> aubio:in_1  
OR
     file -> own:output_1 -> aubio:in_1 

aubio (jack mode) will output to aubio:midi_out_1, so we need to connect
     aubio:midi_out_1 -> own:mini_input_1


###

This is modified based on thru_client.py and play_file.py

"""
import sys
import signal
import os
import jack
import threading
import argparse
try:
    import queue # python 3.x
except ImportError:
    import Queue as queue # python 2.x
    
if sys.version_info < (3, 0):
    # In Python 2.x, event.wait() cannot be interrupted with Ctrl+C.
    # Therefore, we disable the whole KeyboardInterrupt mechanism.
    # This will not close the JACK client properly, but at least we can
    # use Ctrl+C.
    signal.signal(signal.SIGINT, signal.SIG_DFL)
else:
    # If you use Python 3.x, everything is fine.
    pass

argv = iter(sys.argv)
# By default, use script name without extension as client name:
defaultclientname = os.path.splitext(os.path.basename(next(argv)))[0]
clientname = next(argv, defaultclientname)

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('-f', '--filename', default='',
                    help='audio file to be played back')
parser.add_argument(
        '-b', '--buffersize', type=int, default=20,
        help='number of blocks used for buffering (default: %(default)s)')
parser.add_argument('-c', '--clientname', default='file player',
                                        help='JACK client name')
parser.add_argument('-m', '--manual', action='store_true',
                                        help="don't connect to output ports automatically")
args = parser.parse_args()
if args.buffersize < 1:
        parser.error('buffersize must be at least 1')

if args.filename != '':
    print(args.filename)

client = jack.Client(clientname)
blocksize = client.blocksize
samplerate = client.samplerate
print('client:blocksize=', blocksize, ' samplerate=', samplerate)

if client.status.server_started:
    print('JACK server started')
if client.status.name_not_unique:
    print('unique name {0!r} assigned'.format(client.name))

total_blocks_in_file = 0
block_being_get = 0
start_frame = 0
last_actual_time = 0.0
beat_counts = 0
last_beat_counts = 0
last_beat_time = 0.0

event = threading.Event()

# data queuexo
q = queue.Queue(maxsize=args.buffersize)


@client.set_process_callback
def process(frames):
    assert len(client.inports) == len(client.outports)
    assert frames == client.blocksize
    #print('in process() frames=', frames)

    if args.filename != '':
        # feed data into client:output_1
        try:
            data = q.get_nowait()
            #print('data len', len(data.T))
            #global block_being_get
            #print('block[', block_being_get, ']')
            #block_being_get = block_being_get + 1
            #print(data)
        except queue.Empty:
            stop_callback('Buffer is empty: increase buffersize?')
        if data is None:
            stop_callback('playback file is finished.') # playback file is finished
        port = client.outports[0]
        for channel in data.T:
            #print('channel=', channel)
            port.get_array()[:] = channel

    # by now, we have data in client:output_1 (i.e. client.inports[0])
    # and we already connected client:output_1 to aubio:in_1 for aubiotrack processing
    # now we need to get output from aubio:midi_out_1, which should be presented at
    # client:midi_input_1
    i = client.midi_inports[0]
    import binascii
    for offset, data in i.incoming_midi_events():
        #print("{0}: 0x{1}".format(client.last_frame_time+offset,
        #                          binascii.hexlify(data).decode()))
        frame_time = client.last_frame_time+offset
        global start_frame, last_actual_time, last_beat_counts, beat_counts, last_beat_time
        if start_frame == 0:
            start_frame = frame_time
        actual_time = float(frame_time) / samplerate
        if last_beat_time == 0.0:
            last_beat_time = actual_time
        beat_counts = beat_counts + 1
        #print("{0}: 0x{1} :{2}s".format(frame_time - start_frame,
        #                                binascii.hexlify(data).decode(),
        #                                actual_time))
        # we reset beat calculation when there is 3 second gap of beats
        if(last_beat_time + 3.0 < actual_time):
            print('reset last beat counts')
            last_actual_time = actual_time
            last_beat_counts = beat_counts
        if (actual_time - last_actual_time) > 10.0 :
            print('beats=', beat_counts - last_beat_counts,
                  ' bpm = ', (beat_counts - last_beat_counts)/(actual_time - last_actual_time)*60)
            #we could accumulate the counts and calcuate BMP accumulatively
            # or do the following to reset every 10 seconds
            #last_actual_time = actual_time
            #last_beat_counts = beat_counts
        # update last_beat_time    
        last_beat_time = actual_time
                
@client.set_shutdown_callback
def shutdown(status, reason):
    print('JACK shutdown!')
    print('status:', status)
    print('reason:', reason)
    event.set()


# create two port pairs
for number in 1, 2:
    client.inports.register('input_{0}'.format(number))
    client.outports.register('output_{0}'.format(number))
    client.midi_inports.register('midi_input_{0}'.format(number))
    

# open audio file if provided
if args.filename != '':
    import soundfile as sf
    with sf.SoundFile(args.filename) as f:
        print('file channels= ', f.channels)
        block_generator = f.blocks(blocksize=blocksize, dtype='float32',
                                   always_2d=True, fill_value=0)
        total_blocks_in_file = 0
        for _, data in zip(range(args.buffersize), block_generator):
            #print('data size=', len(data), ' ', data[0],data[1],data[2])
            q.put_nowait(data)  # Pre-fill queue
            #global total_blocks_in_file
            total_blocks_in_file = total_blocks_in_file + 1

        print('total blocks in file = ', total_blocks_in_file)

        with client:
            capture = client.get_ports(is_physical=True, is_output=True)
            print('len of capture ports', len(capture))
            if not capture:
                raise RuntimeError('No physical capture ports')
            client.connect(capture[0], client.inports[0])
    
            playback = client.get_ports(is_physical=True, is_input=True)
            if not playback:
                raise RuntimeError('No physical playback ports')

            aubio_inports = client.get_ports('aubio:in_1', is_input=True)
            if not aubio_inports:
                raise RuntimeError('No aubio:in_1 port. You must start aubiotrack -j (in jack mode)')
            client.connect(client.outports[0], aubio_inports[0])

            aubio_midi_outports = client.get_ports('aubio:midi_out_1', is_output=True)
            if not aubio_midi_outports:
                raise RuntimeError('No aubio:midi_out_1 port. You must start aubiotrack -j (in jack mode)')
            client.connect(aubio_midi_outports[0], client.midi_inports[0])

            print('after connects. total blocks in file = ', total_blocks_in_file)

            timeout = float(blocksize) * args.buffersize / samplerate
            print('timeout= ', timeout)
            for data in block_generator:
                q.put(data, timeout=timeout)
                total_blocks_in_file = total_blocks_in_file + 1
            q.put(None, timeout=timeout)  # Signal end of file
            print('final total blocks in file = ', total_blocks_in_file)
        
else: # no file input, use system capture device
    with client:
        capture = client.get_ports(is_physical=True, is_output=True)
        print('len of capture ports', len(capture))
        print(capture)
        if not capture:
            raise RuntimeError('No physical capture ports')
        #client.connect(capture[0], client.inports[0])
    
        #playback = client.get_ports(is_physical=True, is_input=True)
        #if not playback:
        #    raise RuntimeError('No physical playback ports')

        aubio_inports = client.get_ports('aubio:in_1', is_input=True)
        if not aubio_inports:
            raise RuntimeError('No aubio:in_1 port. You must start aubiotrack -j (in jack mode)')
        #client.connect(client.outports[0], aubio_inports[0])
        client.connect(capture[0], aubio_inports[0])

        aubio_midi_outports = client.get_ports('aubio:midi_out_1', is_output=True)
        if not aubio_midi_outports:
            raise RuntimeError('No aubio:midi_out_1 port. You must start aubiotrack -j (in jack mode)')
        client.connect(aubio_midi_outports[0], client.midi_inports[0])

        print('Press Ctrl+C to stop')
        try:
            event.wait()
        except KeyboardInterrupt:
            print('\nInterrupted by user')

# When the above with-statement is left (either because the end of the
# code block is reached, or because an exception was raised inside),
# client.deactivate() and client.close() are called automatically.
