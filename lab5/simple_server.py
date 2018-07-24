#!/usr/bin/env python
# This program acts as a simple server that is capable of connecting to
# a single client using TCP sockets

import socket

group_port = 8007

server_ip = '127.0.0.1'
server_port = group_port

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind( (server_ip, server_port) )
server_socket.listen(5)

print 'Listening on {}:{}'.format(server_ip, server_port)

while True:
    client_socket, client_address = server_socket.accept()
    print 'Connected to client at {}:{}'.format(client_address[0], client_address[1])
    message = raw_input("Type a message to the client: ")
    client_socket.send(message)
    client_socket.close()
