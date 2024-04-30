class Coluna:
    def __init__(self, nome):
        self.nome = nome

    
class Quadro:
    def __init__(self, colunas=[]):
        self.colunas = colunas


    def inserir_colunas(self, coluna):
        self.colunas.append(coluna)