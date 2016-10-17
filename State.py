from Production import *
from Grammar import *
from Functions import *
from copy import *

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
		c = 0
		while c < len(state.productions):
			self.productions.append(state.productions[c])
			c += 1

		if state.final:
			self.final = True
		self.mergeIqualProductions()


	def mergeIqualProductions(self):
		v = 0
		while v < len(self.productions):
			v2 = v + 1
			while v2 < len(self.productions):
				if self.productions[v].symbol == self.productions[v2].symbol:
					self.productions[v].mergeProduction(self.productions[v2])
					self.productions.pop(v2)
					v2 -= 1
				v2 += 1
			v += 1
