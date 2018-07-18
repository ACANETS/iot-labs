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
# @file awsiotsub.py
# @brief AWS IoT subscriber
#

import paho.mqtt.client as paho
import os
import socket
import ssl
import configparser

def on_connect(client, userdata, flags, rc):
    print("Connection returned result: " + str(rc) )
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("#" , 1 )

def on_message(client, userdata, msg):
    print("topic: "+msg.topic)
    print("payload: "+str(msg.payload))

#def on_log(client, userdata, level, msg):
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

#
#mqttc.tls_set(caPath, certfile=certPath, keyfile=keyPath, cert_reqs=ssl.CERT_REQUIRED, tls_version=ssl.PROTOCOL_TLSv1_2, ciphers=None)
# use MQTT over HTTPS (443)
ssl_context= ssl_alpn()
mqttc.tls_set_context(context=ssl_context)
mqttc.connect(awshost, awsport, keepalive=60)
mqttc.loop_forever()
