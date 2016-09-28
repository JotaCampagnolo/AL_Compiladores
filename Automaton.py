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
	
	
	def merge(self, automaton):
		copyAutomaton = deepcopy(automaton)
		pass
		
	
	
    # Funçao que printa o AUTOMATO como tabela:
    def printAutomaton(self):
        tabela = []
        linha = [None]*(len(self.symbols) + 1)
        tabela.append(["*"] + self.symbols)
        for ez in self.states:
            l = linha.copy()
            l[0] = "<" + str(ez.uid) + ">"
            for i in ez.productions:
                c = 1
                for j in self.symbols:
                    if i.symbol == j:
                        a = ""
                        if i.destiny:
                            for k in i.destiny:
                                a += "<" + str(k.uid) + ">" + " "
                                l[c] = a
                        else:	#	Aqui é a producao do estado final
                            l[c] = "#"
                    else:
                        if l[c] == None:
                            l[c] = "#"
                    c += 1
            if ez.final:
                l += [" FINAL"]
            tabela.append(l)
        print(self.name)
        for i in tabela:
            for j in i:
                print("{:6}".format(j), end = "|")
            print()
