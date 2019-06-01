def parse(DATA):
    DATA = DATA.split(b";")
    clientID = DATA[0]
    payload = DATA[1]

    print("ID: {}, Payload: {}".format(clientID, payload))

    if payload == b"None":
        return "202"

    return "200"