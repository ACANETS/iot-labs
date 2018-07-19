# iot lab 4 "Dance with the Music"

People love music and often dance to music. Humans have an instinct to detect the beats in a song, therefore can dance with the rhythm. But how can a computer or an IoT device detect the beats of a music and "dance"? Of course we do not expect an IoT to physically dance, but we could have it compute on the song track to detect beats in order to shine a LED based on the rhythm of the song. This is what we will do in this lab.       

The following topics are covered in this lab:
* I2S bus protocols
* Audio signal processing
* Aubio library
* Jack Audio Connection Kit (JACK)
* Python programming
* Git revision control

## Prerequisites

Please familiarize yourself with the following concepts before proceeding with this lab:
* Digital signal processing. We will need some basic knowledge about DSP, for example, what is FFT and how it works.
* Digital logic. Although most of the sensors require analog input, they produce digital output for microprocessors to process. So we deal with exclusively digital signals, which are based on '0' and '1'. You need to understand the basics of digital logic. You can refer to tutorials such as [this one](https://learn.sparkfun.com/tutorials/digital-logic).
* Linux. We will use Linux throughout this and other labs. It is different from a Windows environment, but you will soon find it liberate us to perform simple and direct control on devices. You need to know basic Linux commands such as ```ls```, ```sudo```, ```nano``` and ```pwd```.
* Python. We primarily use Python as our programming language in these labs. You can of course adapt the examples from Python to other languages, but your mileage varies. So pick up a quick tutorial such as [this one](https://www.learnpython.org) if you are new to it.
* Basics of using Pi Zero W. You should already successfully complete lab 1.

## Procedure

1. Identify the pins of I2S microphone with the following diagram.

![I2S microphone pins](https://cdn-learn.adafruit.com/assets/assets/000/039/629/small360/sensors_pintou.jpg?1487797934)

2. Plug I2S microphone pins into your breadboard. Note that you will use 3.3V power rail as power input instead of 5V.
  * __BLCK__ - master clock to tell microphone when to transmit data
  * __DOUT__ - data output from the microphone
  * __LRCLK__ - left/right clock to tell which channel to transmit. Low for left, High for right.
  * __SEL__ - channel selection pin. Default is low, indicating mono and left channel. If High, it is on the right channel.

3. Identify the GPIO pins (10 and 11) of Pi Zero W with the following diagram.

![PZW Pinouts (pc:pi4y.com)](http://pi4j.com/images/j8header-zero.png)

### __!CAUTION!__ Make sure your Pi is powered off before performing the next steps until 6.

4. Connect the proper pins from your Pi to the microphone. Please ask your teammate or TA to double check the connections.

![Pi with i2S Microphone](https://cdn-learn.adafruit.com/assets/assets/000/039/636/original/sensors_pi_i2s_bb.png?1487800378)

5. Have your teammate and TA double check the connections.

6. Power on the Pi by connecting the USB cable to your laptop. Login as usual.

7. Check if sound card drivers are loaded properly.
```
lsmod | grep snd
```
You should see an output from the command as follows.
![lsmod output](https://cdn-learn.adafruit.com/assets/assets/000/040/622/medium800/sensors_Screen_Shot_2017-04-03_at_11.06.56_AM.png?1491244026)

8. We now check if the microphone is detected properly.
```
cat /proc/asound/cards
arecord -l
```

9. Run the following commands to record an audio sample, and use ```Ctrl+C``` to stop recording. Yes, you can sing to the microphone now ;-)
```
arecord -D plughw:1 -c1 -r 48000 -f S32_LE -t wav -V mono -v file.wav
```

10. Transfer the file ```file.wav``` to your laptop and play back onto a speaker.

### If you can hear what you recorded, you are okay to proceed to the next steps. Otherwise, you need to spend some time on troubleshooting.

11. Try the example program to detect beats per minute of a song.
```
cd ~/iot-labs/lab4
jackd -r -d alsa jackd -r -d alsa -d hw:sndrpisimplecar -r 44100 -n 16 &
```

12. On your smartphone, begin playing your favorite song. Position the phone's speaker a few inches above the I2S microphone. Make sure the speaker is pointed directly at the microphone port, and run the following commands:
```
aubiotrack -j &
./detect_bpm.py
```

13. Continue playing the song for about 30 seconds. The beats-per-minute should be printed to the screen.

14. When you are finished, press Ctrl+C and run the following command to reset aubiojack:
```
killall aubiojack
```

15. Repeat steps 12 though 14 with different songs. Try to experiment with both fast and slow songs.
