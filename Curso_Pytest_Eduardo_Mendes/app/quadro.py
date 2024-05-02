from dataclasses import dataclass

@dataclass
class Tarefa:
    nome: str

class Coluna:
    def __init__(self, nome, tarefas):
        self.nome = nome
        self.tarefas = []

    def __getitem__(self, item):
        return self.tarefas[item]

    def insere_tarefa(self, tarefa):
        self.tarefas.append(tarefa)

    def remover_tarefas(self, tarefa):
        self.tarefas.remove(tarefa)

    def __repr__(self) -> str:
        return f'Coluna(nome="{self.nome}", tarefa="{self.tarefas}")'

    
class Quadro:
    def __init__(self, colunas=None):
        self.colunas = colunas or []


    def inserir_coluna(self, coluna):
        self.colunas.append(coluna)

    def inserir_tarefa(self, tarefa):
        self.colunas[0].insere_tarefa(tarefa)

    def remover_tarefas(self, tarefa):
        self.tarefas.remove(tarefa)

    def mover(self, tarefa):
        if tarefa in self.colunas[0]:
            self.colunas[0].remover_tarefas(tarefa)
            self.colunas[1].insere_tarefa(tarefa)