class Tarefa:
    def __init__(self, nome):
        self.nome = nome

class Coluna:
    def __init__(self, nome):
        self.nome = nome
        self.tarefas = []

    def insere_tarefa(self, tarefa):
        ...

        
class Quadro:
    def __init__(self, colunas=[], tarefas=[]):
        self.colunas = colunas
        self.tarefas = tarefas

    def inserir_coluna(self, coluna):
        self.colunas.append(coluna)

    def inserir_tarefa(self, tarefa):
        self.colunas[0].insere_tarefa(tarefa)
        # self.tarefas.append(tarefa)

