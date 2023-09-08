from bytebank import Funcionario

def test_idade():
    teste_01 = Funcionario('carlos', '03/11/1985', 3139)
    teste_02 = Funcionario('mayara', '04/01/1985', 3139)
    teste_03 = Funcionario('neto', '31/10/2015', 3139)

    print(f'Teste = {teste_01.idade()}')
    print(f'Teste = {teste_02.idade()}')
    print(f'Teste = {teste_03.idade()}')

test_idade()