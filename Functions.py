from Production import *
from State import *
from Grammar import *

def readInput(file_name):
    try:
        f = open(file_name)
    except:
        print('Could not open the file: "' + file_name + '"')

    inputList = []
    tokensList = []
    grammars = []
    tempGrammar = []

    for i in f:
        inputList.append(i)

    numTokens = int(inputList[0].replace('\n', ""))

    #   Coloca em tokensList os tokens do arquivo
    for i in inputList[1:numTokens + 1]:
        tokensList.append(i.replace('\n', ""))

    for i in inputList[numTokens+1:]:
        if i == "\n":
            if tempGrammar:
                grammars.append(tempGrammar)
                tempGrammar = []
        else:
            tempGrammar.append(i.replace("\n", ""))
    if tempGrammar:
        grammars.append(tempGrammar)

    return [tokensList, grammars]


def firstn():
    num = 1
    while True:
        yield num
        num += 1
