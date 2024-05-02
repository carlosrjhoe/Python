from app.quadro import Quadro, Coluna, Tarefa
from pytest import fixture
import factory

class QuadroFactory(factory.Factory):
    class Meta:
        model = Quadro

    colunas = [Coluna('A'), Coluna('B')]

class ColunasFactory(factory.Factory):
    class Meta:
        model = nomes

    colunas = [Coluna('A'), Coluna('B')]

@fixture
def factory_boy_test():
    return QuadroFactory.build()

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
  