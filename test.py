from Grammar import *
from State import *
from Production import *
from Automaton import *
import subprocess
import sys

a = sys.argv[1]
b = sys.argv[2]


def testa(file_name1, file_name2):
	#	Abre o arquivo de teste
	try:
		in1 = open(file_name1)
	except:
		print('Could not open the file: "' + file_name1 + '"')
		exit()

	#	Abre o arquivo de resposta
	try:
		an = open(file_name2)
	except:
		print('Could not open the file: "' + file_name2 + '"')
		exit()


	fList = []
	for i in in1:
		fList.append(i.replace('\n', ""))

	gra = Grammar("Gramatica 1", fList)
	aut = Automaton("Automato da " + gra.name, gra)
	ans = aut.printAutomaton()
	resp = ""
	c = 0

	for i in an:
		resp += i

	if resp == ans:
		print("Teste de", file_name1, "passou no teste")
	else:
		print("Teste de", file_name1, "reprovou no teste *")


testa(a, b)
