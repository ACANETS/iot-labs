# iot lab 5 "Let's Talk"

IoT depends on Internet to connect the devices to other parts of the world. Internet is built on top of a set of network protocols such as IP, TCP/UDP, HTTP, etc. Network protocols are standards defining how machines should "talk" to each other over computer networks. We use this lab to demonstrate the network programming and practice useful tools to analyze network activities.         

The following topics are covered in this lab:
* Network protocols
* Packet headers
* Tcpdump and libpcap library
* Network programming

## Prerequisites

Please familiarize yourself with the following concepts before proceeding with this lab:
* Networking. We will need some basic knowledge about computer networking, which includes network protocols, packets, routing, etc. A good tutorial on computer networking can be found [here](http://www.steves-internet-guide.com/basic-networking-course/) .
* Linux. We will use Linux throughout this and other labs. It is different from a Windows environment, but you will soon find it liberate us to perform simple and direct control on devices. You need to know basic Linux commands such as ```ls```, ```sudo```, ```nano``` and ```pwd```.
* Python. We primarily use Python as our programming language in these labs. You can of course adapt the examples from Python to other languages, but your mileage varies. So pick up a quick tutorial such as [this one](https://www.learnpython.org) if you are new to it.
* Basics of using Pi Zero W. You should already successfully complete lab 1.

## Procedure

1. Power on the Pi by connecting the USB cable to your laptop. Login as usual over SSH.

2. Follow the instructions of [network setting on Mac or Windows](https://learn.adafruit.com/turning-your-raspberry-pi-zero-into-a-usb-gadget/ethernet-gadget). Test the network connection by running the following commands (if you are running Windows, PuTTY should connect via SSH automatically, you do not need to run these commands): 
```
ping raspberrypi.local 
ssh pi@raspberrypi.local
```

3. Open a second terminal window (Mac/Unix) or PuTTY client (Windows) and login to the device again over SSH by running the following commands (if you are running Windows, PuTTY should connect via SSH automatically, you do not need to run these commands):
```
ping 192.168.7.2
ssh pi@192.168.7.2
```

4. In both terminal windows, navigate to the lab5 directory
```
cd ~/iot-labs/lab5
```

5. In one SSH session, run the following command:
```
./simple_server.py
```

6. The server should begin listening on address 127.0.0.1. In the other SSH session, run the client command:
```
./simple_client.py
```

7. Go back to the SSH session running the simple server. It should have a new connection from a client, and prompt you to input a string. Type a message to send to the client and press enter.

8. Looking at the client window, you should see the message you typed appear in the output. The client will then disconnect from the server.

9. In the terminal running the server, press Ctrl+C to stop running the server.

10. You will now use tcpdump to monitor packets being sent back and forth using the ssh protocol. In one of the two terminal windows, enter the following command:
```
tcpdump port ssh -i usb0 -w capture.pcap
```

11. tcpdump will be monitoring all packets that are passed over the SSH protocol. In the other terminal window, enter the following commands to list the files in the directory.
```
ls
ll
ls -lah
```

12. Go back to the terminal window running tcpdump and press Ctrl+C to terminate command. On the host machine, execute the following command to transfer the 'capture.pcap' file for analysis using wireshark.
```
scp pi@raspberrypi.local:~/iot-labs/lab5/capture.pcap .
```

13. Use wireshark to analyze the file.
