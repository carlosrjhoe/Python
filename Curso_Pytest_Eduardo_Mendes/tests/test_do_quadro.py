from app.quadro import Quadro, Coluna, Tarefa
from pytest import fixture

@fixture
def quadro():
    print('Executa antes dos testes...')
    return Quadro()

def test_nao_deve_existir_nenhuma_coluna_no_quadro(quadro):
    quantidade_de_colunas = len(quadro.colunas)
    assert quantidade_de_colunas == 0

def test_quando_inserir_coluna_deve_existir_coluna(quadro):
    quadro.inserir_colunas(Coluna(nome='A fazer'))
    assert len(quadro.colunas) == 1

def test_quando_inserir_a_coluna_a_fazer_ele_deve_estar_no_quadro(quadro):
    assert quadro.colunas[0].nome == 'A fazer'

def test_quando_inserir_uma_tarefa_no_quadro_ela_deve_estar_na_primeira_coluna(quadro):
    quadro.inserir_tarefa(Tarefa(nome='Dormir'))
    assert len(quadro.colunas[0].tarefas) == 1