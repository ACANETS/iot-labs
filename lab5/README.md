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

1. Power on the Pi by connecting the USB cable to your laptop. Login as usual.

2. Check the network interfaces on Pi.
```
ifconfig
```
You should see an output from the command as follows.
![ifconfig output](/images/lab2_ifconfig.png)

3. We now check if your Pi is connected to the Internet.
```
ping google.com
```

4. Run the example program.
```
cd ~/iot-labs/lab5
./net_example.py
```

5. Explain what the example program does.

6. Use tcpdump to capture packet traces.
