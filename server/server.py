#!/usr/bin/env python3

# imports
import socket
import importlib
from ServerParse import parser


# server info
HOST = '127.0.0.1' # localhost
PORT = 3000 # port to listen on
SERVER = (HOST, PORT)


# server config
IPv4 = socket.AF_INET
TCP = socket.SOCK_STREAM


# client info
clientList = []


# setup
with socket.socket(IPv4, TCP) as s:
    s.bind(SERVER)
    s.listen()
    print("Listening on {}:{}".format(HOST, PORT))
    conn, addr = s.accept()
    cid = conn.recv(1024)
    clientList.append((cid, addr))
    with conn:
        print("Connection at {}!".format(addr[0]))
        

        while True:
            importlib.reload(ServerParse)
            data = conn.recv(1024)
            conn.sendall(data)

    print("Connection Disconnected!")