import re

def parse(DATA):
    DATA = DATA.split(b";")
    clientID = DATA[0]
    payload = DATA[1]

    commands = {
#        Command  : Description
        b"searcha": [SearchA, "Search by artist name."], # implement this one first, then the other 2
        b"searchs": "Search by song name.",
        b"searchf": "Search by file name."
        }

    print("ID: {}, Payload: {}".format(clientID, payload))

    if payload == b"None":
        return "202"

    payload = payload.split(b",")

    err = 0
    for command in payload:
        func = command.split(b" ")[0].lower()
        arguments = [arg.lower() for arg in command.split(b" ")[1:]]
        print("func: {}, args: {}".format(func, arguments))
        if func not in commands.keys():
            err += 1
        else:
            commands[func][0](arguments)

    return ("200" if err == 0 else str(300 + err))

def SearchA(ArtistName):
    """ 
        Searches for ArtistName in 'IDindex.txt'\n
        Because list is passed in, only uses first entry.
    """
    ArtistName = str(ArtistName[0])
    print("In SearchA, param = " + ArtistName)