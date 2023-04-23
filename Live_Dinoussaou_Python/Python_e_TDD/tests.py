from unittest import TestCase
from problema import problema

class TestProblema(TestCase):
    """
        [x] A -> Existem numeros positivos
        [x] B -> Não existem numeros positivos -> 1
        [x] C -> Lista vazia -> 1
        [x] D -> Não exitem numeros faltantes -> LAST + 1
    """
  
    def test_problema_de_retornar_5(self):
        esperado = 6
        resultado = problema([ 3, 4, 5, 0, 1, -14, 20, 2, 7, 10, -2])
        self.assertEqual(esperado, resultado)

    def test_problema_de_retornar_1(self):
        esperado = 1
        resultado = problema([ -14, -20, -2, -7, -10, -2])
        self.assertEqual(esperado, resultado)
        
    def test_problema_de_retornar_1_quando_nao_houver_elementos_na_lista(self):
        esperado = 1
        resultado = problema([])
        self.assertEqual(esperado, resultado)

    def test_problema_de_retornar_ultimo_mais_1_quando_nao_houver_numero_faltante(self):
        esperado = 10
        resultado = problema([1,2,3,4,5,6,7,8,9])
        self.assertEqual(esperado, resultado)
    
    