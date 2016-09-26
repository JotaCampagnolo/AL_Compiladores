# Classe que define uma PRODUÇAO:
class Production:
    def __init__(self, name, father):
        self.name = name        # Nome da produçao recebido por parametro. Exemplo: "a <B>".
        self.father = father    # Pai da produçao, ou seja, recebe o estado (nao terminal) que a possue como produçao.
        self.destiny = []       # O destino da produçao e o nao terminal contido na produçao.
        self.symbol = None      # E o simbolo nao terminal da producao.

        splited = name.split(" ")
        if len(splited[0]) > 2:
            if splited[0] == "<" and splited[len(splited) - 1] == ">":
                # Achou um estado
                
