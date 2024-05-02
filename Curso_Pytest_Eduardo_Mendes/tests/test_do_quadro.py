from app.quadro import Coluna, Tarefa


def test_nao_deve_existir_nenhuma_coluna_no_quadro(quadro):
    quantidade_de_colunas = len(quadro.colunas)
    assert quantidade_de_colunas == 0

def test_quando_inserir_coluna_deve_existir_coluna(quadro):
    quadro.inserir_coluna(Coluna(nome='A fazer'))
    assert len(quadro.colunas) == 1

def test_quando_inserir_a_coluna_a_fazer_ele_deve_estar_no_quadro(quadro):
    assert quadro.colunas[0].nome == 'A fazer'

def test_quando_inserir_uma_tarefa_no_quadro_ela_deve_estar_na_primeira_coluna(quadro,quadro_com_coluna):
    quadro_com_coluna.inserir_tarefa(Tarefa(nome='Dormir'))
    assert len(quadro.colunas[0].tarefas) == 1

def test_quando_inserir_a_segunda_tarefas_no_quadro_ela_deve_estar_na_primeira_coluna(quadro,quadro_com_coluna):
    quadro_com_coluna.inserir_tarefa(Tarefa(nome='Dormir'))
    quadro_com_coluna.inserir_tarefa(Tarefa(nome='Comer'))
    assert len(quadro_com_coluna.colunas[0].tarefas) == 3

def test_quando_mover_cartao_ele_deve_ir_para_coluna_seguinte(quadro_com_colunas):
    tarefa = Tarefa('Usar Mascara')
    quadro_com_colunas.inserir_tarefa(tarefa)
    quadro_com_colunas.mover(tarefa)
    assert tarefa in quadro_com_colunas.colunas[1]