Para adicionar casos de teste, crie dois arquivos (entrada e resposta), no
seguinte padrão:
    arq_de_entrada.in:
        <S> ::= a <A> | b <B>
        <A> ::= a <A> | a
        <B> ::= b <B> | b

    arq_de_resposta.an:
        Automato da Gramatica 1
        *     |a     |b     |
        1     |2     |3     |
        2     |2     |-     | FINAL|
        3     |-     |3     | FINAL|

Coloque os arquivos no diretório testcases/ e adicione a
tupla ("testcases/arq_de_entrada.in", "testcases/arq_de_resposta.an") na lista
de testes do arquivo Tests.py:
...
    tests = [("testcases/t1.in", "testcases/t1.an"),
             ("testcases/t2.in", "testcases/t2.an"),
             ("testcases/arquivo_de_entrada.in", "testcases/arquivo_de_resposta.an")]
...


Para executar os testes, execute o programa Tests.py:
$ python3 Tests.py
