class Tarefa:
    def __init__(self, nome):
        self.nome = nome

class Quadro:
    def __init__(self, colunas=[], tarefas=[]):
        self.colunas = colunas
        self.tarefas = tarefas

    def inserir_coluna(self, coluna):
        self.colunas.append(coluna)

    def inserir_tarefa(self, tarefa):
        self.tarefas.append(tarefa)


class Coluna:
    def __init__(self, nome):
        self.nome = nome