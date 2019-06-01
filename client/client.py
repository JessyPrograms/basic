#!/usr/bin/env python3

import socket

HOST, PORT = "127.0.0.1", 3000

identifier = "Id3n713r".encode()

IPv4 = socket.AF_INET
TCP = socket.SOCK_STREAM

sdata = ""

with socket.socket(IPv4, TCP) as s:
    s.connect((HOST, PORT))
    s.sendall(identifier)
    while sdata != b"exit":
        com = input("==> ")
        if not com:
            com = "None"

        sdata = len(identifier) + ";" + identifier + ";" + len(com) + ";" + com

        s.sendall(sdata.encode())
        
