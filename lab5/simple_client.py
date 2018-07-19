#!/usr/bin/env python
import socket

server_ip = '127.0.0.1'
server_port = 30001

print 'Attempting to connect to server at {}:{}'.format(server_ip, server_port)

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect((server_ip, server_port))

print client_socket.recv(1024)

client_socket.close()
