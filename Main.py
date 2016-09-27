from Grammar import *
from State import *
from Production import *
from Functions import *

#   inputs[0] eh a lista de tokens
#   inputs[1] eh a lista de gramaticas brutas
inputs = readInput("input.txt")
grammars = []

# Instanciaçao das gramaticas a partir da lista de TOKENS:
for i in inputs[0]:
    grammars.append(Grammar("Gramatica " + i, i))

# Instanciaçao das gramaticas a partir da lista de GRAMATICAS:
count = 1
for i in inputs[1]:
    grammars.append(Grammar("Gramatica " + str(count), i))
    count += 1

# Criaçao das GRAMATICAS (Classe Grammar):
for i in grammars:
    i.createGrammar()
    i.printGrammar()
