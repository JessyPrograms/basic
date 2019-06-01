#!/usr/bin/env python3

import socket
import importlib
import ServerParser


HOST = '127.0.0.1' # localhost
PORT = 3000 # port to listen on
SERVER = (HOST, PORT)

IPv4 = socket.AF_INET
TCP = socket.SOCK_STREAM

clientList = []

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
            importlib.reload(ServerParser)
            data = conn.recv(1024)

            if not data:
                break

            sdata = ServerParser.parse(data)

            if sdata != None:
                conn.sendall(sdata)

print("Connection Disconnected!")