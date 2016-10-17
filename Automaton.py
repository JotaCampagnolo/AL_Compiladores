from Grammar import *
from State import *
from Production import *
from Functions import *
from copy import *

class Automaton:
	def __init__(self, name, grammar):
		self.name = name
		self.grammar = grammar
		self.states = self.grammar.states
		self.symbols = grammar.symbols
		self.finalStates = [(State("", next(uid), self.grammar), self)]
		self.finalStates[0][0].final = True
		self.states.append(self.finalStates[0][0])
		self.inicializa()
		self.mergeIqualProductions()


	def __str__(self):
		return self.printAutomaton()

	def __add__(self, b):
		c = deepcopy(self)
		d = deepcopy(b)

		k = 0
		while k < len(d.states[0].productions):
			c.states[0].productions.append(d.states[0].productions[k])
			k += 1

		k = 1
		while k < len(d.states):
			c.states.append(d.states[k])
			k += 1

		c.mergeIqualProductions()
		c.finalStates += d.finalStates

		return c


	def inicializa(self):
		c = 0
		while c < len(self.states):
			if self.states[c].final:
				a = 0
				while a < len(self.states[c].productions): # Percorre todas as produções dos estados que são finais
					if not self.states[c].productions[a].destiny: # Se a produção não tiver destino
						self.states[c].productions[a].destiny.append(self.finalStates[0][0])
					a += 1
			c += 1

	# Função para mesclar produções iguais no mesmo estado.
	#	Ex.: a <A> | a <B>  ---> a <A> <B>
	def mergeIqualProductions(self):
		c = 0
		while c < len(self.states):
			v = 0
			while v < len(self.states[c].productions):
				# v2 está um índice a frente de v.
				v2 = v + 1
				### MUDAR A COMPARAÇÂO PORQUE QUANDO DA O POP MUDA O TAMANHO DA LISTA DE PRODUÇÔES ###
				while v2 < len(self.states[c].productions):
					# Se as duas produções tem symbol igual, mescla os destinos na primeira produção (v)
					# e remove da lista de produções a segunda produção (v2), para não repetir.
					if self.states[c].productions[v].symbol == self.states[c].productions[v2].symbol:
						self.states[c].productions[v].mergeProduction(self.states[c].productions[v2])
						self.states[c].productions.pop(v2)
						v2 -= 1
					v2 += 1
				v += 1

			c += 1





	def determinization(self):
		global uid
		dic = {}
		dic["a b"] = JIOSAHDOISA
		c0 = 0
		while c0 < len(self.states):
			c1 = 0
			while c1 < len(self.states[c0].productions):
				if len(self.states[c0].productions[c1].destiny) > 1:	# Achou um indeterminismo, porra
					c2 = 0
					while c2 < len(self.states[c0].productions[c1].destiny):
						d += self.states[c0].productions[c1].destiny[c2].name
						if d in dic:
							pass
						else:
							pass
						c2 += 1
				c1 += 1
			c0 += 1











	# Funçao que printa o AUTOMATO como tabela:
	def printAutomaton(self):
		PRINT = ""
		tabela = []
		linha = ['-']*(len(self.symbols) + 1)
		tabela.append(["*"] + self.symbols)

		for i in self.states:
			newLine = ['-']*(len(self.symbols) + 1)
			newLine[0] = str(i.uid)
			cond = True

			c = 0
			while cond:
				count = 0
				for k in self.symbols:
					if i.productions: # Se não for o estado terminal vazio
						if i.productions[c].symbol == k:
							if i.productions[c].destiny:
								dest = ""
								for p in i.productions[c].destiny:
									dest += str(p.uid) + " "
								newLine[count+1] = dest
						count += 1
				c += 1
				if c > len(i.productions)-1:
					cond = False
					break
			if i.final:
				newLine.append(" FINAL")
			tabela.append(newLine)

		PRINT += self.name + "\n"
		for i in tabela:
			for j in i:
				PRINT += ("{:10}".format(j) + "|")
			PRINT += "\n"
		return PRINT
