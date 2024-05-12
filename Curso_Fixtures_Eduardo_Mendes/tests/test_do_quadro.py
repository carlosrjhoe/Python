from app import Quadro

def test_não_deve_existir_coluna_no_quadro():
    quadro = Quadro() # Dado
    quantidade_colunas = len(quadro.colunas)
    assert quantidade_colunas == 0