#!/usr/bin/env python3

import client
from importlib import reload
from time import sleep

HOST = '127.0.0.1' # localhost
PORT = 3000 # port to listen on
IDENTIFIER = "1337"

while True:
    sleep(2)
    reload(client)
    client.client(HOST, PORT, IDENTIFIER)