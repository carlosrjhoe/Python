from app.quadro import Quadro, Coluna, Tarefa
from pytest import fixture

@fixture
def quadro():
    print('Executa antes dos testes...')
    return Quadro()

@fixture
def quadro_com_coluna(quadro):
    quadro.inserir_coluna(Coluna('A'))
    return quadro

@fixture
def quadro_com_colunas(quadro_com_coluna):
    quadro_com_coluna.inserir_coluna(Coluna('A'))
    return quadro_com_coluna
  