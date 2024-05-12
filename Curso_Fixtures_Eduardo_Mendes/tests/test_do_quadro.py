from app import Quadro, Coluna, Tarefa
from pytest import fixture

@fixture
def setUp():
    print('Estou montando o contexto!')
    return Quadro()


def test_não_deve_existir_coluna_no_quadro(setUp):
    quadro = setUp # Dado
    quantidade_colunas = len(quadro.colunas)
    assert quantidade_colunas == 0

def test_quando_inserir_uma_tarefa_no_quadro_deve_estar_na_primeira_coluna(setUp):
    quadro = setUp # Dado
    quadro.inserir_tarefa(Tarefa(nome='Dormir'))

def test_quando_inserir_uma_coluna_deve_existir_uma_coluna(setUp):
    quadro = setUp # Dado
    quadro.inserir_coluna(Coluna(nome='A fazer')) #
    quantidade_de_colunas = quadro.colunas #
    assert len(quantidade_de_colunas) == 1

def test_quando_inserir_uma_coluna_A_Fazer_ela_deve_estar_no_quadro(setUp):
    quadro = setUp # Dado
    quadro.inserir_coluna(Coluna(nome='A fazer')) #
    assert quadro.colunas[0].nome == 'A fazer'