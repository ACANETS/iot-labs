# iot lab 6 "Say Cheese"

Wouldn't it be fun if we have a camera on the IoT device to take pictures or even videos?  How cool if your IoT can tell you your cat just smiled to the camera? If you are adventurous enough with playing with images and cameras, you will find a lot of fun in this lab. We will show you how to program the Pi to snap pictures, perform face recognition and try to classify the objects in the picture.          

The following topics are covered in this lab:
* Camera sensors
* OpenCV
* Face detection
* Caffe: computer vision with deep learning

## Prerequisites

Please familiarize yourself with the following concepts before proceeding with this lab:
* Computer vision. You will need some basic knowledge about computer vision, and a tutorial can be found  [here](FIXME) .
* OpenCV. It is the most popular computer vision software library. Read this [OpenCV introduction](https://docs.opencv.org/3.2.0/d1/dfb/intro.html).
* Deep Learning. This is the hot topic in almost every industry now. You should know the [basics of Deep Learning](https://medium.com/@shridhar743/a-beginners-guide-to-deep-learning-5ee814cf7706).
* Linux. We will use Linux throughout this and other labs. It is different from a Windows environment, but you will soon find it liberate us to perform simple and direct control on devices. You need to know basic Linux commands such as ```ls```, ```sudo```, ```nano``` and ```pwd```.
* Python. We primarily use Python as our programming language in these labs. You can of course adapt the examples from Python to other languages, but your mileage varies. So pick up a quick tutorial such as [this one](https://www.learnpython.org) if you are new to it.
* Basics of using Pi Zero W. You should already successfully complete lab 1.

## Procedure

__!CAUTION: Your Pi Zero W should be powered off now until you complete step 1 !__

1. Connect the ribbon cable between your Pi Zero W and the Pi Camera v2. (We use the one without IR.) Have your teammate or TA to verify the cable is properly connected on both ends.

2. Power on the Pi by connecting the USB cable to your laptop. Login as usual.

3. Take a picture with your Pi.
```
raspistill -o testimg.jpg
```
You should see the picture file (testimg.jpb) created.

4. Transfer the file to your laptop to view. Note that replace 'YOURGROUP' and 'FILESERVER' with the information provided by the instructor.
```
scp testimg.jpg YOURGROUP@FILESERVER:
```

5. On your laptop, you can view the image uploaded to the file server by visiting FILESERVER in a Web browser. Your old image file will be overwritten if you do not choose a new file name.

3. We now check if your Pi is connected to the Internet.
```
ping google.com
```

4. Run the example program.
```
cd ~/iot-labs/lab6
./face_detection.py
```

5. Explain what the example program does.

6. Send the picture to Caffe image classification framework.
```
./test_caffe.py image_file_name
```
