from codigo.bytebank import Funcionario

class TestClass:
    def test_quando_idade_recebe_03_11_1985_deve_receber_38(self):
        entrada = '03/11/1985/'
        esperado = 38
        funcionario_test = Funcionario('carlos', entrada, 3139)
        resultado = funcionario_test.idade()

        assert resultado == esperado