# iot lab 1 "Hello IoT"

There are millions of IoT devices out there and each has its own functionalities and purposes. Under the hood, they are essentially an embedded devices with some types of sensors and a microprocessor to process the sensor data. We use [Raspberriy Pi Zero W](https://www.raspberrypi.org/products/raspberry-pi-zero-w/) as our experimental platform because it is equipped with versatile interfaces and adequate processing capability. What is more, itself costs only USD $10!     

The following topics are covered in this lab:
1. Boot up the Pi and login
2. Setup network connection
3. Obtain source code and revision control
4. GPIO and circuit wiring
5. Python programming

## Prerequisites

Please familiarize yourself with the following concepts before proceed with this lab:
* Linux. We will use Linux throughout this and other labs. It is different from a Windows environment, but you will soon find it liberate us to perform simple and direct control on devices. You need to know basic Linux commands such as ```ls```, ```sudo```, ```nano``` and ```pwd```.
* Python. We primarily use Python as our programming language in these labs. You can of course adapt the examples from Python to other languages, but your mileage varies. So pick up a quick tutorial such as [this one](https://www.learnpython.org) if you are new to it.
* You need to have a laptop with at least one USB2.0 or USB3.0 port to run the labs. Windows, Mac, Linux laptops should all work, but we have not tested on USB-C ports.
* You will be provided with a raspberry-pi-zero-w, a MicroSD card, a USB to TTL-serial cable, a breadboard, a LED and, 330 Ohm resistor, and assorted jumper cables.

## Procedure

1. Install driver for USB to TTL-serial adapter. Plug in the USB cable to your laptop. If it is not recognized automatically, you need to install software for the adapter cable on your laptop. See instructions for [Windows](https://learn.adafruit.com/adafruits-raspberry-pi-lesson-5-using-a-console-cable/software-installation-windows), [Mac](https://learn.adafruit.com/adafruits-raspberry-pi-lesson-5-using-a-console-cable/software-installation-mac), or [Linux](https://learn.adafruit.com/adafruits-raspberry-pi-lesson-5-using-a-console-cable/software-installation-linux))

2. Connect the Pi Zero W to the TTL serial leads. Please proceed with __!CAUTION!__

  i. __!CAUTION!__ Make sure the USB end is disconnected from your laptop.

  ii. __!CAUTION!__ Make sure the colored leads are connected to the correct PINs on the Pi. Refer to the following diagram for connection.

  ![PZW Pinouts (pc:pi4y.com)](http://pi4j.com/images/j8header-zero.png)
  ![TTL-serial to PZW (pc:adafruit.com)](https://learn.adafruit.com/assets/41071)

  iii. Have your teammate and TA to help double check the connections.

3. Insert MicroSD card to the card slot on Pi Zero W.

4. Connect the USB end to your laptop.

5. Open terminal software on your laptop to watch the boot process and wait for login prompt.

6. Login with user ```pi``` and the password given by the instructor.

7. Run command ```pwd```. You should see ```/home/pi``` as the result of this command. If so, then run ```ll``` to see the list of files in your home directory.

8. Now, we need to shutdown the Pi and prepare the LED circuit. Run command ```sudo halt```. Wait for the green LED on the Pi to be off. Then unplug the USB-TTL cable from your laptop.

### Your Pi Zero W should be off now before you proceed with the following steps.

9. Wire up the following circuit to connect a LED to the GPIO pin of Pi. Have your teammate and the TA to double check your wiring.

  ![PZE with GPIO LED (pc:medium.com)](https://cdn-images-1.medium.com/max/1600/0*xch19X3RFpIZdFXw.png)

10. Boot up your Pi Zero W again. After login to the Linux, use git command to retrieve the source code from repository like this

```git clone http://github.com/ACANETS/iot-labs```

11. Run the example code by using the following command:

```
cd iot-labs
./toggleled.py
```

12. You should now see the LED is toggled between ON and OFF.
