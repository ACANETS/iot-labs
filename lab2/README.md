# iot lab 2 "I am HoT"

IoT plays an important role in our life is because the IoT devices are capable of sensing. Sensors, as an integral part of an IoT device, enable us to monitor the environment and observe activities that we as human may not be able to see or experience in person. Therefore, it is necessary for us to understand the principles of sensors, how to interface with sensors, and how to program them.      

The following topics are covered in this lab:
1. I<sup>2</sup>C bus and interfacing.
2. I<sup>2</sup>C programming
3. Python programming
4. Obtain source code and revision control

## Prerequisites

Please familiarize yourself with the following concepts before proceeding with this lab:
* Digital logic. Although most of the sensors require analog input, they produce digital output for microprocessors to process. So we deal with exclusively digital signals, which are based on '0' and '1'. You need to understand the basics of digital logic. You can refer to tutorials such as [this one](https://learn.sparkfun.com/tutorials/digital-logic).
* Linux. We will use Linux throughout this and other labs. It is different from a Windows environment, but you will soon find it liberate us to perform simple and direct control on devices. You need to know basic Linux commands such as ```ls```, ```sudo```, ```nano``` and ```pwd```.
* Python. We primarily use Python as our programming language in these labs. You can of course adapt the examples from Python to other languages, but your mileage varies. So pick up a quick tutorial such as [this one](https://www.learnpython.org) if you are new to it.
* Basics of using Pi Zero W. You should already successfully complete lab 1.

## Procedure

1. Identify the pins of I<sup>2</sup>C MCP9808 temperature sensor with the following diagram.

![MCP9808 pins](https://cdn-learn.adafruit.com/assets/assets/000/015/726/original/adafruit_products_2.png?1396474366)

2. Plug the sensor pins into your breadboard.

3. Identify the I<sup>2</sup>C connectors (SCL, SDA) on GPIO9 and GPIO8, as well as PWR and GND pins of Pi Zero W with the following diagram.

![PZW Pinouts (pc:pi4y.com)](http://pi4j.com/images/j8header-zero.png)

### __!CAUTION!__ Make sure your Pi is powered off before performing the next step.

4. Connect the proper pins from your Pi to the temperature sensor. Please ask your teammate or TA to double check the connections.

5. Power on the Pi and login.

6. Run command ```ls /dev/*i2c*```. You should see ```/dev/i2c-1``` as the output of this command. If not, you need to contact the instructor, or follow [an advanced tutorial](https://learn.sparkfun.com/tutorials/raspberry-pi-spi-and-i2c-tutorial) to enable I<sup>2</sup>C on the Pi.

7. Run the command as follows to see if your temperature sensor is detected. You should see the number ```18```. If not, you must power off the Pi and check the wiring before you proceed.
```
pi@raspberrypi:~/$ i2cdetect -y 1
     0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f
00:          -- -- -- -- -- -- -- -- -- -- -- -- --
10: -- -- -- -- -- -- -- -- 18 -- -- -- -- -- -- --
20: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
30: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
40: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
50: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
60: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
70: -- -- -- -- -- -- -- --
```

8. Run the following commands to execute the example program.
```
cd ~/iot-labs/lab2
python ./read_temp.py C
```

You can change the temperature units by changing the argument (the C, for celcius) to an F (fahrenheit) or a K (kelvin).

9. Explain what the example program does.
