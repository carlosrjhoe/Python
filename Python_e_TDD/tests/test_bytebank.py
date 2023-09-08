from codigo.bytebank import Funcionario

class TestClass:
    
    def test_quando_idade_recebe_03_11_1985_deve_receber_38(self):
        """
        DADO a data de nascimento
        QUANDO o metodo idade é chamada
        ENTÃO deve retornar a idade
        """
        entrada = '03/11/1985'
        esperado = 38
        funcionario_test = Funcionario('carlos', entrada, 3139)
        resultado = funcionario_test.idade()

        assert resultado == esperado

    def test_quando_sobrenome_recebe_carlos_conceicao_deve_retornar_conceicao(self):
        """
        DADO um nome com sobrenome
        QUANDO o metodo sobre_nome é chamado
        ENTÃO deve retornar o sobrenome
        """
        entrada = 'carlos conceição'
        esperado = 'conceição'
        funcionario_test = Funcionario('carlos conceição', entrada, 3139)
        resultado = funcionario_test.sobre_nome()

        assert resultado == esperado
