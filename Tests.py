import subprocess

erros = []
acertos = []


tests = [("testcases/t1.in", "testcases/t1.an"),
		 ("testcases/t2.in", "testcases/t2.an"),
		 ("testcases/t3.in", "testcases/t3.an"),
		 ("testcases/t4.in", "testcases/t4.an"),
		 ("testcases/t5.in", "testcases/t5.an"),
		 ("testcases/t6.in", "testcases/t6.an")]
for i in tests:
	try:
		output = subprocess.check_output("python3 test.py " + i[0] + " " + i[1], shell=True).decode('utf-8').replace("\n", "")
		print(output)
		if output[len(output)-1] == '*':
			erros += [i[0]]
		else:
			acertos += [i[0]]
	except:
		erros += [i[0]]
		print("Ocorreu uma excecao ao executar", i[0])

print("\nTestes concluidos")
print("Total de erros:", len(erros))
print("Total de acertos:", len(acertos))

if erros:
    print("Testes que não passaram:")
    for i in erros:
        print(i)
