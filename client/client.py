#!/usr/bin/env python3

import socket

errcodes = {
#    Code : Description
    b"200": "OK",
    b"202": "Confirmed None",
    b"300": "invalid command",
    b"404": "Result not found",
    b"500": "There was an unknown error.",
    }

def client(HOST, PORT):
    sdata = ""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        while sdata != b"exit":
            sdata = input("==> ")
            if not sdata:
                sdata = "None"
            if sdata == "exit":
                break

            s.sendall(sdata.encode())

            DATA = s.recv(1024)
            print(DATA)
