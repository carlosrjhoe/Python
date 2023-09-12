from codigo.bytebank import Funcionario
from pytest import raises, mark

class TestClass:

    def test_quando_nome_recebe_carlos_deve_retornar_carlos(self):
        """
        GIVEN: o nome recebe carlos
        WHEN: o metodo nome é chamada
        THEN: deve retornar a nome
        """
        esperado = 'Carlos Conceição'
        funcionario_test = Funcionario('Carlos Conceição', '03/11/1985', 3139)
        resultado = funcionario_test._nome

        assert resultado == esperado

    def test_quando_salario_recebe_3139_deve_retornar_3139(self):
        """
        GIVEN: o salario recebe 3139
        WHEN: o metodo salario é chamada
        THEN: deve retornar a salario
        """
        esperado = 3139
        funcionario_test = Funcionario('Carlos Conceição', '03/11/1985', 3139)
        resultado = funcionario_test._salario

        assert resultado == esperado
        
    def test_quando_data_de_nascimento_recebe_03_11_1985_deve_retornar_38(self):
        """
        GIVEN: a data de nascimento
        WHEN: o metodo idade é chamada
        THEN: deve retornar a idade
        """
        esperado = 38
        funcionario_test = Funcionario('Carlos Conceição', '03/11/1985', 3139)
        resultado = funcionario_test.idade()

        assert resultado == esperado

    def test_sobrenome_conceicao_e_verificado_na_funcao_eh_socio_deve_retornar_true(self):
        """
        GIVEN: sobrenome
        WHEN: o metodo eh_socio é chamada
        THEN: deve retornar TRUE se o sobrenome consta na lista de sobrenommes
        """
        esperado = True
        funcionario_test = Funcionario('Carlos Conceição', '03/11/1985', 3139)
        resultado = funcionario_test.eh_socio()

        assert resultado == esperado
        
    def test_quando_sobrenome_recebe_carlos_conceicao_deve_retornar_conceicao(self):
        """
        GIVEN: um nome com sobrenome
        WHEN: o metodo sobre_nome é chamado
        THEN: deve retornar o sobrenome
        """
        esperado = 'Conceição'
        funcionario_test = Funcionario('Carlos Conceição', '03/11/1985', 3139)
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
        funcionario_test = Funcionario('Carlos Conceição', '03/11/1985', 100000)
        resultado = funcionario_test.desconto()

        assert resultado == esperado

    @mark.calcular_bonus
    def test_quando_calcular_bonus_recebe_1000_deve_retornar_100(self):
        """
        GIVEN: um valor do salario
        WHEN: o metodo calcular_bonus é chamado
        THEN: deve retornar o bonus de R$100.00 
        """
        entrada = 1000
        esperado = 100
        funcionario_test = Funcionario('Carlos Conceição', '03/11/1985', entrada)
        resultado = funcionario_test.calcular_bonus()
        
        assert esperado == resultado

    @mark.calcular_bonus
    def test_quando_calcular_bonus_recebe_100000_deve_retornar_exception(self):
        """
        GIVEN: um valor do salario
        WHEN: o metodo calcular_bonus é chamado
        THEN: deve retornar um exceptionError
        """
        with raises(Exception):
            entrada = 100000
            funcionario_test = Funcionario('Carlos Conceição', '03/11/1985', entrada)
            resultado = funcionario_test.calcular_bonus()
            
            assert resultado

    def test_quando_vuncao__str__retorna_instancia_de_Funcionario(self):
        """
        GIVEN: um nome, data de nascimento e salario
        WHEN: o metodo __str__() é chamado
        THEN: deve retornar por extenso o nome, data de nascimento e salario
        """
        nome, data_nascimento, salario = 'Carlos Conceição', '3/11/1985', 3139
        esperado = 'Funcionario(Carlos Conceição, 3/11/1985, 3139)'
        funcionario_test = Funcionario(nome, data_nascimento, salario)
        resultado = funcionario_test.__str__()

        assert resultado == esperado