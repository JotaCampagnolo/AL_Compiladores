from Imports import *

uid = firstn()

# Classe que define uma GRAMATICA:
class Grammar:
    def __init__(self, name, generator):
        self.name = name        # Nome da gramatica (else, por exemplo).
        self.states = []

        if type(generator) == type("string"):
            self.generator = tokenToGrammar(generator)       # Quando o parametro gerador for um token.
        elif type(generator) == type([]):
            self.generator = generator      # Quando o parametro gerador for uma gramatica.

    def createGrammar(self):
        global uid
        grammarTable = []

        # Intancia os estados sem produçoes:
        for i in self.generator:
            aux = i.split(" ::= ")
            grammarTable.append(aux)
            self.states.append(State(aux[0], next(uid), self))

        
