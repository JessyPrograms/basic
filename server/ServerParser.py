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

def genPacket(DATA, ERRS):
    """
        returns a structured packet to send to client\n
        DATA:ERRS\n
        code,result;code,result:code,result\n
        result is space seperated
    """
    # searcha yes,test hello,searcha no -- test data
    sdata = ""
    if len(DATA) >= 1:
        for i in DATA:
            datadelist = " ".join(i[1])
            sdata += "{},{};".format(i[0], "".join(datadelist))
        sdata = sdata[:-1]
    else:
        sdata += "202,None"
    sdata += ":"
    if len(ERRS) >= 1:
        for i in ERRS:
            # ['300', ['test', ['hello']]]
            i[1][1] = " ".join(i[1][1])
            i[1] = " ".join(i[1])
            sdata += "{},{};".format(i[0], i[1])
        sdata = sdata[:-1]
    else:
        sdata += "202,None"
    return sdata




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

    stopexc = False
    results = []
    incrctfunc = []
   

    if payload == b"None":
        stopexc = True


    if not stopexc:
        payload = payload.split(b",")

        err = 0

        for command in payload:
            func = command.split(b" ")[0].lower() # gets the function
            arguments = [arg.lower() for arg in command.split(b" ")[1:]]
            # print("func: {}, args: {}".format(func, arguments))
            if func not in commands.keys():
                err += 1
                incrctfunc.append(["300", [func.decode(), [i.decode() for i in arguments]]])
            else:
                # must return a list [responseCode, result]
                results.append(commands[func][0](arguments))
    return genPacket(results, incrctfunc)
    


def search(asf, name):
    """
        Searches through IDindex list, using asf as an index for inner list.
        returns if EXACT match found.
    """
    if asf < 0 or asf >=4:
        print("Invalid ASF")
        return ["500", ["None"]]

    for i in IDindex:
        # print("{} {} {}".format(i[asf], "=" if i[asf] == name else "!=", name))
        if i[asf] == name:
            return ["200", i]
    return ["404", ["Not Found"]]
            


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
    return searchResult
        
