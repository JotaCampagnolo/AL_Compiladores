from State import *
from Production import *
from Functions import *

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

        self.grammarTable = []

    def createGrammar(self):
        global uid

        # Intancia os estados sem produçoes:
        for i in self.generator:
            aux = i.split(" ::= ")
            self.grammarTable.append(aux)
            newState = State(aux[0], next(uid), self)
            self.states.append(newState)

        # Instancia as produçoes de cada estado:
        count = 0
        for i in self.states:
            i.addProductions(self.grammarTable[count][1])
            count += 1

    # Retorna o Estado cujo nome eh igual ao nome passado por parametro:
    def returnState(self, name):
        count = 0
        for i in self.grammarTable:
            if i[0] == name:
                return self.states[count]
            count += 1
        return False

    # Funçao que printa a Gramatica:
    def printGrammar(self):
        print(self.name + ":")
        for i in self.states:
            print("(" + str(i.uid) + ")", i.name, "::= ", end="")
            for j in i.productions:
                print(j.name, "| ", end="")
            if i.final:
                print(" Final", end="")
            print()
