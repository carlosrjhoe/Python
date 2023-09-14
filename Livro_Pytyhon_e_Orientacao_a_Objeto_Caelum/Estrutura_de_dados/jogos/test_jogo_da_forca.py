from forca import cabecalho

class TestClass:

    def test_cabecalho(self):
        """
        GIVEN: função cabecalho
        WHEN: o metodo cabecalho é chamada
        THEN: deve retornar o texto "BEM VIDO AO JOGO DA FORCA"
        """
        esperado = 'BEM VIDO AO JOGO DA FORCA'
        assert esperado == cabecalho()