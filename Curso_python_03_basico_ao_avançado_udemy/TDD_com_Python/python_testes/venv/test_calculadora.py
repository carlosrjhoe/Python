import unittest
from Calculadora import soma

class testCalculadora(unittest.TestCase):
    def test_soma_5_e_5_deve_retornar_10(self):
        self.assertEqual(soma(5,5), 10)

    def test_soma_5_negativo_e_5_deve_retornar_0(self):
        self.assertEqual(soma(-5,5), 0)

    def test_soma_varias_entradas(self):
        x_y_saidas = (
            (10, 10, 20),
            (1.5, 1.5, 3.0),
            (10, 30, 40),
            (100, 10, 110),
            (120, 150, 270),
        )
        
        for x_y_saida in x_y_saidas:
            x, y, saida = x_y_saida
            self.assertEqual(soma(x, y), saida)

    def test_soma_x_nao_e_int_ou_float_deve_retornar_assertionerror(self):
        with self.assertRaises(AssertionError):
            soma('11', 0)

    def test_soma_y_nao_e_int_ou_float_deve_retornar_assertionerror(self):
        with self.assertRaises(AssertionError):
            soma(11, '0')

    
unittest.main(verbosity=2)