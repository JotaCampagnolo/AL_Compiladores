from Production import *
from Grammar import *
from Functions import *

# Classe que define um ESTADO:
class State:
	def __init__(self, name, uid, father):
		self.name = name            # Nome do estado, recebido por parâmetro.
		self.uid = uid              # Identificador unico recebido pelo gerador de identificadores.
		self.father = father        # O pai de um estado é a gramatica que o contem.
		self.final = False          # Todo estado e instanciado como final, e modificado a cada producao adicionada.
		self.productions = []       # Lista de produçoes do estado, que inicia como vazia.

	def addProduction(self, generator):
		p = Production(generator, self)
		self.productions.append(p)

	def addProductions(self, generator):
		productions = generator.split(" | ")
		for i in productions:
			# Verifica se eh £ produçao, se for, o estado vira final e a produçao nao eh adicionada:
			if not (i == "£"):
				self.addProduction(i)
			else:
				self.final = True

	def merge(self, state):
		pass
