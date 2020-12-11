#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 16:55:20 2020

@author: edoardottt
"""

import socket
import threading

bind_ip = "127.0.0.1"
bind_port = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((bind_ip, bind_port))

server.listen(5)

print("[*] Listening on {}:{}".format(bind_ip, bind_port))

# this is our client-handling thread
def handle_client(client_socket):

    # print out what the client sends
    request = client_socket.recv(4096)

    print("[*] Received: {}".format(request))

    # send back a packet
    client_socket.send(b"ACK!")

    client_socket.close()


while True:
    client, addr = server.accept()

    print("[*] Accepted connection  from {}:{}".format(addr[0], addr[1]))

    # spin up our client thread to handle incoming data
    client_handler = threading.Thread(target=handle_client, args=(client,))

    client_handler.start()