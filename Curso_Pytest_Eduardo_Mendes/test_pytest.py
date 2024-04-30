from calculadora import soma, subtrair, mutiplicar, dividir, mutiplicar_por_0

def test_quando_soma_receber_1_e_2_entao_deve_retornar_3():
    x = 1
    y = 2
    assert soma(x, y) == 3

def test_quando_subtrair_receber_2_e_1_entao_deve_retornar_1():
    x = 2
    y = 1
    assert subtrair(x, y) == 1

def test_quando_mutiplicar_receber_2_e_2_entao_deve_retornar_4():
    x = 2
    y = 2
    assert mutiplicar(x, y) == 4

def test_quando_dividir_receber_4_e_2_entao_deve_retornar_2():
    x = 4
    y = 2
    assert dividir(x, y) == 2
    
def test_quando_mutiplicar_receber_0_entao_deve_retornar_0():
    x = 0
    y = 2
    assert mutiplicar_por_0(x, y) == 0

def test_de_soma_deve_escrever_entrei_na_soma(capsys):
    x = 2
    y = 2
    soma(x, y)
    resultado = capsys.readouterr()
    assert resultado.out == 'Entrei na soma\n'