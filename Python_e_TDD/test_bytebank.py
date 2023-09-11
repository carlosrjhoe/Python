from codigo.bytebank import Funcionario
from pytest import raises, mark

class TestClass:
    
    def test_quando_data_de_nascimento_recebe_03_11_1985_deve_retornar_38(self):
        """
        GIVEN: a data de nascimento
        WHEN: o metodo idade é chamada
        THEN: deve retornar a idade
        """
        esperado = 38
        funcionario_test = Funcionario('carlos', '03/11/1985', 3139)
        resultado = funcionario_test.idade()

        assert resultado == esperado

    def test_quando_sobrenome_recebe_carlos_conceicao_deve_retornar_conceicao(self):
        """
        GIVEN: um nome com sobrenome
        WHEN: o metodo sobre_nome é chamado
        THEN: deve retornar o sobrenome
        """
        esperado = 'conceição'
        funcionario_test = Funcionario('carlos conceição', '03/11/1985', 3139)
        resultado = funcionario_test.sobre_nome()

        assert resultado == esperado

    # @mark.skip
    def test_quando_desconto_recebe_salario_deve_ser_descontado_10_por_cento(self):
        """
        GIVEN: um valor do salario
        WHEN: o metodo desconto é chamado
        THEN: deve retornar o salario com desconto de 10 por cento
        """
        esperado = 90000
        funcionario_test = Funcionario('carlos conceição', '03/11/1985', 100000)
        resultado = funcionario_test.desconto()

        assert resultado == esperado

    @mark.calcular_bonus
    def test_quando_calcular_bonus_recebe_1000_deve_retornar_100(self):
        """
        GIVEN: um valor do salario
        WHEN: o metodo desconto é chamado
        THEN: deve retornar o bonus de R$100.00 
        """
        entrada = 1000
        esperado = 100
        funcionario_test = Funcionario('carlos conceição', '03/11/1985', entrada)
        resultado = funcionario_test.calcular_bonus()
        
        assert esperado == resultado

    @mark.calcular_bonus
    def test_quando_calcular_bonus_recebe_100000_deve_retornar_exception(self):
        with raises(Exception):
            entrada = 100000
            funcionario_test = Funcionario('carlos conceição', '03/11/1985', entrada)
            resultado = funcionario_test.calcular_bonus()
            
            assert resultado
