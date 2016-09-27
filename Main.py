from Grammar import *
from State import *
from Production import *
from Functions import *

#   inputs[0] eh a lista de tokens
#   inputs[1] eh a lista de gramaticas brutas
inputs = readInput("input.txt")

gramatica1 = Grammar("Gramatica 01", inputs[1][0])
gramatica1.createGrammar()
gramatica1.printGrammar()

gramatica2 = Grammar("Gramatica 02", inputs[1][1])
gramatica2.createGrammar()
gramatica2.printGrammar()
