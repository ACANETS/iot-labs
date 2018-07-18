#!/usr/bin/python3

#
# Copyright 2018. Yan Luo. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License").
# You may not use this file except in compliance with the License.
# A copy of the License is located at
#
#  https://www.apache.org/licenses/LICENSE-2.0
#
# or in the "license" file accompanying this file. This file is distributed
# on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either
# express or implied. See the License for the specific language governing
# permissions and limitations under the License.
#

#
# @file awsiotpub.py
# @brief AWS IoT publisher
#

import paho.mqtt.client as paho
import os
import socket
import ssl
from time import sleep
from random import uniform
import configparser
import json

connflag = False

def on_connect(client, userdata, flags, rc):
    global connflag
    connflag = True
    print("Connection returned result: " + str(rc) )

def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))


#def on_log(client, userdata, level, buf):
#    print(msg.topic+" "+str(msg.payload))

mqttc = paho.Client()
mqttc.on_connect = on_connect
mqttc.on_message = on_message
#mqttc.on_log = on_log

# get IOT parameters from ini file
config = configparser.ConfigParser()
config.read('aws_iot_config.ini')
certspath = config['DEFAULT']['AWS_IOT_CERTS_PATH']
awshost = config['DEFAULT']['AWS_IOT_MQTT_HOST']
awsport = int(config['DEFAULT']['AWS_IOT_MQTT_PORT'])
clientID = config['DEFAULT']['AWS_IOT_MQTT_CLIENT_ID']
thingName = config['DEFAULT']['AWS_IOT_MY_THING_NAME']
caPath = certspath+config['DEFAULT']['AWS_IOT_ROOT_CA_FILENAME']
certPath = certspath+config['DEFAULT']['AWS_IOT_CERTIFICATE_FILENAME']
keyPath = certspath+config['DEFAULT']['AWS_IOT_PRIVATE_KEY_FILENAME']

sn = config['DEFAULT']['SN']
city = config['LOCATION']['CITY']
state = config['LOCATION']['STATE']

print('caPath is ', caPath)
print('certPath is ', certPath)
print(' keyPath is ', keyPath)

# we require ALPN protocol extension for MQTT over HTTPS (443)
# which requires python3 due to the need of OpenSSL 1.0.2 or later.
IoT_protocol_name = "x-amzn-mqtt-ca"
def ssl_alpn():
    try:
        #debug print opnessl version
        print("open ssl version:{}".format(ssl.OPENSSL_VERSION))
        ssl_context = ssl.create_default_context()
        ssl_context.set_alpn_protocols([IoT_protocol_name])
        ssl_context.load_verify_locations(cafile=caPath)
        ssl_context.load_cert_chain(certfile=certPath, keyfile=keyPath)
        return  ssl_context
    except Exception as e:
        print("exception ssl_alpn()")
        raise e

# set up TLS parameters for MQTTC
#mqttc.tls_set(caPath, certfile=certPath, keyfile=keyPath, cert_reqs=ssl.CERT_REQUIRED, tls_version=ssl.PROTOCOL_TLSv1_2, ciphers=None)
# use MQTT over HTTPS (443)
ssl_context= ssl_alpn()
mqttc.tls_set_context(context=ssl_context)
mqttc.connect(awshost, awsport, keepalive=60)
mqttc.loop_start()


topic = "ThingRegister"
message = json.dumps({ "clientID": clientID, "thingName" : thingName,
                       "location": state+"-"+city, "SN": sn})
mqttc.publish(topic, message, qos=1)
print("msg sent: " + topic + " " + message )

topic = "Temperature"
while 1==1:
    sleep(1)
    if connflag == True:
        # we use a random number for now.
        tempreading = uniform(20.0,25.0)
        message = json.dumps({ "clientID": clientID, "temperature": tempreading,
                               "location": state+"-"+city,"SN": sn})
        mqttc.publish(topic, message, qos=1)
        print("msg sent: " + topic + " %.2f" % tempreading )
    else:
        print("waiting for connection...")
