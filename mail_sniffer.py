#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 19:25:19 2020

@author: edoardottt
"""

from scapy.all import *

# our packet callback
def packet_callback(packet):
    print(packet.show())
    
# fire up our sniffer
sniff(filter="",prn=packet_callback,count=1)