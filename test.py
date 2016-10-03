from Grammar import *
from State import *
from Production import *
from Automaton import *
from Functions import *
import subprocess
import os

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
		print("Teste de", file_name1, "reprovou no teste")



tests = [("testcases/t1.in", "testcases/t1.an"),
		 ("testcases/t2.in", "testcases/t2.an")]
for i in tests:
	testa(i[0], i[1])
