"""
Numeros = [0, 3, 10, -2, -14, 20]
"""

from unittest import TestCase
from problema import problema

class TestProblema(TestCase):
    """
    [ ] A -> Existem n numeros positivos
    [ ] B -> Não existem numeros positivos -> 1
    [ ] C -> Lista vazia -> 1
    [ ] D -> Não exitem numeros faltantes -> LAST + 1
    """
  
    def test_problema_de_retornar_5(self):
        esperado = 6
        resultado = problema([ 3, 4, 5, 0, 1, -14, 20, 2, 7, 10, -2])

        self.assertEqual(esperado, resultado)

    def test_problema_de_retornar_1(self):
        esperado = 1
        resultado = problema([ -14, -20, -2, -7, -10, -2])

        self.assertEqual(esperado, resultado)
    
    