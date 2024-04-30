from app.quadro import Quadro, Coluna

def test_nao_deve_existir_nenhuma_coluna_no_quadro():
    quadro = Quadro()
    quantidade_de_colunas = len(quadro.colunas)
    assert quantidade_de_colunas == 0

def test_quando_inserir_coluna_deve_existir_coluna():
    quadro = Quadro()
    quadro.inserir_colunas(Coluna(nome='A fazer'))
    assert len(quadro.colunas) == 1

def test_quando_inserir_a_coluna_a_fazer_ele_deve_estar_no_quadro():
    quadro = Quadro()
    assert quadro.colunas[0].nome == 'A fazer'