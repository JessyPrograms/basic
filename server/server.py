#!/usr/bin/env python3

import importlib
import socket

import ServerParser


def Server(HOST, PORT):
    clientList = []
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print("Listening on {}:{}".format(HOST, PORT))
        conn, addr = s.accept()
        cid = conn.recv(1024)
        clientList.append(cid)
        with conn:
            print("Connection at {}!".format(addr[0]))
            
            while True:
                importlib.reload(ServerParser)
                data = conn.recv(1024)

                if not data:
                    break
                    
                # sdata = response code
                sdata = ServerParser.parse(data)

                if sdata != None:
                    conn.sendall(sdata.encode())
    print("Connection Disconnected!")
    return
