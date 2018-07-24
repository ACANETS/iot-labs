#!/usr/bin/env python
import socket

group_port = 0

server_ip = '127.0.0.1'
server_port = group_port

print 'Attempting to connect to server at {}:{}'.format(server_ip, server_port)

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect((server_ip, server_port))

print client_socket.recv(1024)

client_socket.close()
