#!/usr/bin/env python3

import socket

HOST = '127.0.0.1' # localhost
PORT = 3000 # port to listen on

IPv4 = socket.AF_INET
TCP = socket.SOCK_STREAM

with socket.socket(IPv4, TCP) as s:
    s.bind((HOST, PORT))
    s.listen()
    print("Listening on {}:{}".format(HOST, PORT))
    conn, addr = s.accept()
    with conn:
        print("Connection at {}!".format(addr[0]))
        while True:
            data = conn.recv(1024)
            if not data:
                break
            print("Received from {} = Data Size: {}, Data[:12]: {}".format(addr[0], len(data), data[:12]))
            conn.sendall(data)
    print("Connection Disconnected!")