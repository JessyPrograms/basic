#!/usr/bin/env python3

import client
import importlib

HOST = '127.0.0.1' # localhost
PORT = 3000 # port to listen on

while True:
    importlib.reload(server)
    server.Server(HOST, PORT)