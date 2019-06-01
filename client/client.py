#!/usr/bin/env python3

import socket

errcodes = {
#    Code : Description
    b"200": "OK",
    b"202": "Confirmed None",
    b"300": "3XX, XX represents no. of invalid commands.",
    b"404": "There was an unknown error.",
    }

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

            realCode = s.recv(1024)
            try:
                if int(realCode) >= 300 and int(realCode) < 400:
                    checkCode = b"300"
                else:
                    checkCode = realCode
            except ValueError:
                realcode = b"404"
                checkCode = b"404"
            finally:
                print("{} - {}".format(
                    realCode,
                    errcodes[checkCode] if checkCode in errcodes.keys() else "Unknown Error Code!"
                ))
            
            
            
