from Production import *
from Grammar import *
from Functions import *

# Classe que define um ESTADO:
class State:
    def __init__(self, name, uid, father):
        self.name = name            # Nome do estado recebido por parametro.
        self.uid = uid              # Identificador unico recebido pelo gerador de identificadores.
        self.father = father        # O pai de um estado e a gramatica que o contem.
        self.final = False          # Todo estado e instanciado como final, e modificado a cada producao adicionada.
        self.productions = []       # Lista de produçoes do estado, que inicia como vazia.

    def addProduction(self, generator):
        self.productions.append(Production(generator, self))

    def addProductions(self, generator):
        productions = generator.split(" | ")
        for i in productions:
            self.addProduction(i)
