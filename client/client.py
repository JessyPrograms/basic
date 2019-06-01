#!/usr/bin/env python3

import socket

errcodes = {b"200": "OK", b"202": "Confirmed None"}

def client(HOST, PORT, IDENTIFIER):
    sdata = ""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(IDENTIFIER.encode())
        while sdata != b"exit":
            com = input("==> ")
            if not com:
                com = "None"
            if com == "exit":
                break

            sdata = "{};{}".format(IDENTIFIER, com)
            s.sendall(sdata.encode())

            responseCode = s.recv(1024)
            print(
                "{} - {}".format(
                    responseCode,
                    errcodes[responseCode] if responseCode in errcodes.keys() else "Unknown Error Code!"
                )
            )
            
