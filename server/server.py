#!/usr/bin/env python3

import importlib
import socket

import ServerParser


def Server(HOST, PORT):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
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
                    
                importlib.reload(ServerParser)
                sdata = ServerParser.parse(data)

                if sdata != None:
                    try:
                        conn.sendall(sdata.encode())
                    except :
                        print("invalid something in sendall - server")
                    
    print("Connection Disconnected!")
    return
