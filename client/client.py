#!/usr/bin/env python3

import socket

HOST, PORT = "127.0.0.1", 3000

IPv4 = socket.AF_INET
TCP = socket.SOCK_STREAM

sdata = ""

with socket.socket(IPv4, TCP) as s:
    s.connect((HOST, PORT))
    while sdata != b"exit":
        sdata = input("==> ").encode()
        s.sendall(sdata)
        data = s.recv(1024)
