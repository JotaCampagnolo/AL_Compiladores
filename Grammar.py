# Classe que define uma GRAMATICA:
class Grammar:
    def __init__(self, name, generator):
        self.name = name        # Nome da gramatica (else, por exemplo).
        if type(generator) == type("string"):
            tokenToGrammar(generator)       # Quando o parametro gerador for um token.
        elif type(generator) == type([]):
            self.generator = generator      # Quando o parametro gerador for uma gramatica.
