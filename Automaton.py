from Grammar import *
from State import *
from Production import *
from Functions import *
from copy import *

class Automaton:
	def __init__(self, name, grammar):
		self.name = name
		self.grammar = grammar
		self.states = grammar.states
		self.symbols = grammar.symbols
		self.printAutomaton()

	def __str__(self):
		return self.printAutomaton()

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
				PRINT += ("{:6}".format(j) + "|")
			PRINT += "\n"
		return PRINT
