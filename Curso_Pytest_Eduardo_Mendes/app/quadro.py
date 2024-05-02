from dataclasses import dataclass

@dataclass
class Tarefa:
    nome: str

class Coluna:
    def __init__(self, nome):
        self.nome = nome
        self.tarefas = []

    def insere_tarefa(self, tarefa):
        self.tarefas.append(tarefa)

    def __repr__(self) -> str:
        return f'Coluna(nome="{self.nome}", tarefa="{self.tarefas}")'

    
class Quadro:
    def __init__(self, colunas=[]):
        self.colunas = colunas


    def inserir_coluna(self, coluna):
        self.colunas.append(coluna)

    def inserir_tarefa(self, tarefa):
        self.colunas[0].insere_tarefa(tarefa)