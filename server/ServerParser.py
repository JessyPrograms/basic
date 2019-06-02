def openIDindex():
    """
        creates a list containing lists from parsed lines of 'IDindex.txt'
    """
    data = []
    with open("cal500/IDindex.txt", "r") as f:
        # 5th_dimension-one_less_bell_to_answer	TRVZZOL12519AA54F9 -- example line
        for line in f:
            line = line.split("\t")
            line[0] = line[0].split("-")
            line[1] = line[1].strip()
            artist = line[0][0]
            song = line[0][1]
            filename = line[1]
            data.append([artist, song, filename])
    return data


IDindex = openIDindex()


def parse(DATA):
    """
        Parser function for parsing data sent from client
    """

    payload = DATA

    commands = {
#        Command  : Description
        b"searcha": [SearchA, "Search by artist name."], # implement this one first, then the other 2
        b"searchs": "Search by song name.",
        b"searchf": "Search by file name."
        }

    if payload == b"None":
        return "202"

    payload = payload.split(b",")

    err = 0
    for command in payload:
        func = command.split(b" ")[0].lower() # gets the function
        arguments = [arg.lower() for arg in command.split(b" ")[1:]]
        print("func: {}, args: {}".format(func, arguments))
        if func not in commands.keys():
            err += 1
        else:
            code = commands[func][0](arguments)
            return "200" if code == None else "404"
    return ("200" if err == 0 else str(300 + err))


def search(asf, name):
    """
        Searches through IDindex list, using asf as an index for inner list.
        returns if EXACT match found.
    """
    if asf < 0 or asf >=4:
        print("Invalid ASF")
        return b"404"

    
    for i in IDindex:
        # print("{} {} {}".format(i[asf], "=" if i[asf] == name else "!=", name))
        if i[asf] == name:
            return i
    return b"404"
            


def SearchA(ArtistName):
    """ 
        Searches for ArtistName in 'IDindex.txt'\n
        Because list is passed in, only uses first entry.
        use "_" instead of " "
    """
    # 5th_dimension-one_less_bell_to_answer	TRVZZOL12519AA54F9 -- example line
    # ["5th_dimension", "one_less_bell_to_answer", "TRVZZOL12519AA54F9"] -- example parsed line
    ArtistName = ArtistName[0].decode()

    searchResult = search(int(0), ArtistName)

    if type(searchResult) == bytes:
        return str(searchResult)

    print("Results = " + str(searchResult))
        
