# iot lab 3 "Shine the Lights"

Light is magical. LEDs have become the center of attention because new advance in LED technology enables many interesting products and designs. LEDs are much brighter and more colorful. The applications of new LEDs are fun and limitless. In this lab, we will play with a LED type called "DotStar" and learn how to program them to make special light effects.      

The library used in this lab is supplied by Adafruit (www.adafruit.com).

The following topics are covered in this lab:
* SPI bus and interfacing
* Level shifting
* Python programming
* Git revision control

## Prerequisites

Please familiarize yourself with the following concepts before proceeding with this lab:
* Digital logic. Although most of the sensors require analog input, they produce digital output for microprocessors to process. So we deal with exclusively digital signals, which are based on '0' and '1'. You need to understand the basics of digital logic. You can refer to tutorials such as [this one](https://learn.sparkfun.com/tutorials/digital-logic).
* Linux. We will use Linux throughout this and other labs. It is different from a Windows environment, but you will soon find it liberate us to perform simple and direct control on devices. You need to know basic Linux commands such as ```ls```, ```sudo```, ```nano``` and ```pwd```.
* Python. We primarily use Python as our programming language in these labs. You can of course adapt the examples from Python to other languages, but your mileage varies. So pick up a quick tutorial such as [this one](https://www.learnpython.org) if you are new to it.
* Basics of using Pi Zero W. You should already successfully complete lab 1.

## Procedure

1. Identify the pins of 74AHCT125 level shifter with the following diagram.

![74AHCT125 pins](https://cdn-learn.adafruit.com/assets/assets/000/028/914/original/raspberry_pi_level-shifter.png?1449376887)

2. Plug 74AHCT125 pins into your breadboard.

3. Identify the GPIO pins (10 and 11) of Pi Zero W with the following diagram.

![PZW Pinouts (pc:pi4y.com)](http://pi4j.com/images/j8header-zero.png)

### __!CAUTION!__ Make sure your Pi is powered off before performing the next steps until 9.

4. Connect the proper pins from your Pi to the level shifter. Please ask your teammate or TA to double check the connections.

5. Identify the DAT and CLK pins from DotStar strip.

6. Connect the DAT and CLK pins to the proper pins of 74AHCT125. See the diagram above.

7. Connect the battery pack (with 3 AA batteries) to the breadboard. __!CAUTION! Make sure the battery pack is switched off__ Use a separate 5V power rail on the breadboard, different from the 3.3V power for Pi's pins.

8. Have your teammate and TA double check the connections.

9. Power on the Pi by connecting the USB cable to your laptop. Login as usual.

10. Switch on the battery pack.

11. Run the following commands to execute the example program.
```
cd ~/iot-labs/lab3
sudo python setup.py install
./test_dotstar.py
```

12. Explain what the example program does.
