def deezStringer(deezMinputs):
    deezString = "deeznuts"
    if len(deezMinputs) == 0:
        return "deez nuts"
    retString = "Well why don't you " + deezMinputs + " "
    for i in range(len(deezMinputs)):
        retString += deezString[i%8] + " "
    return retString
