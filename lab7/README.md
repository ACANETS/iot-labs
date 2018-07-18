# iot lab 7 "Over the Rainbow"

It is time to build up a cloud services upon your IoT devices. An IoT cloud service that controls IoT devices, aggregate sensor data and analyze data for business intelligence will enable unprecedented understanding of our physical world. The benefits of cloud computing and cloud services come from the elastic computing capability and always-on nature of the design. In this lab, we will look into how to design a cloud service to gather data from the IoT device you built from previous labs.           

The following topics are covered in this lab:
* MQTT, HTTPS
* AWS IoT, publish/subscribe
* AWS DynamoDB
* AWS EC2

## Prerequisites

Please familiarize yourself with the following concepts before proceeding with this lab:
* Cloud Computing. There are many introductions, and here is [one of them](https://www.explainthatstuff.com/cloud-computing-introduction.html).
* [Amazon Web Services](https://d1.awsstatic.com/whitepapers/aws-overview.pdf).
* IoT protocols. Please read this [survey of IoT protocols](https://www.postscapes.com/internet-of-things-protocols/)
* Linux. We will use Linux throughout this and other labs. It is different from a Windows environment, but you will soon find it liberate us to perform simple and direct control on devices. You need to know basic Linux commands such as ```ls```, ```sudo```, ```nano``` and ```pwd```.
* Python. We primarily use Python as our programming language in these labs. You can of course adapt the examples from Python to other languages, but your mileage varies. So pick up a quick tutorial such as [this one](https://www.learnpython.org) if you are new to it.

## Procedure

1. Check your Pi Zero W to make sure it is connected to Internet. You can simply login and use ```lynx```, the text browser to visit www.google.com.

2. Run the example publisher and subscriber programs.
```
cd ~/iot-labs/lab7
python3 awsiotpub.py &
python3 awsiotsub.py
```
Note the "&" sign after awsiotpub.py command, which put the publisher running in background so we can run the subscriber.

3. Explain what the example programs do. Take a note about the "city" where your IoT device is "deployed".

4. Open a web browser on your laptop and visit the IoT dashboard. Look for the city on the map within the IoT Dashboard. Do you see your temperature number reported and refreshed periodically?

5. The instructor will demonstrate the services on AWS including IoT, EC2 and DynamoDB.
