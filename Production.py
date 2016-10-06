from State import *
from Grammar import *
from Functions import *

# Classe que define uma PRODUÇAO:
class Production:
	def __init__(self, name, father):
		self.name = name        # Nome da produçao recebido por parametro. Exemplo: "a <B>".
		self.father = father    # Pai da produçao, ou seja, recebe o estado (nao terminal) que a possue como produçao.
		self.destiny = []       # O destino da produçao e o nao terminal contido na produçao.
		self.symbol = None      # E o simbolo nao terminal da producao.

		splited = name.split(" ")
		# Verifica se o primeiro simbolo eh terminal ou nao terminal:
		if len(splited[0]) > 2:
			self.destiny.append(self.father.father.returnState(splited[0])) # Funcao que retorna o estado correspondente ao simbolo nao terminal encontrado.
			self.symbol = splited[1]
			# Verifica se o symbolo ja esta na lista de simbolos da Gramatica:
			if self.symbol not in self.father.father.symbols:
				self.father.father.symbols.append(self.symbol)
		else:
			self.symbol = splited[0]
			# Verifica se o symbolo ja esta na lista de simbolos da Gramatica:
			if self.symbol not in self.father.father.symbols:
				self.father.father.symbols.append(self.symbol)
			if len(splited) > 1:
				self.destiny.append(self.father.father.returnState(splited[1])) # Funcao que retorna o estado correspondente ao simbolo nao terminal encontrado.
			else:
				self.father.final = True
    
    # Função para mesclar produções. Adiciona no seu destino os destinos
    # da produção passada por parâmetro
	def mergeProduction(self, prod):
		for i in prod.destiny:
			self.destiny.append(i)
			
