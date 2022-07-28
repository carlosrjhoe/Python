from unittest import TestCase, main

def soma(a, b):
    return a + b

def subitracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    return a / b

class Testes(TestCase):
    def test_soma(self):
        self.assertEqual(soma(2, 2), 4)
    
    def test_subitracao(self):
        self.assertEqual(subitracao(2, 2), 0)
    
    def test_multiplicacao(self):
        self.assertEqual(multiplicacao(2, 2), 4)
    
    def test_divisao(self):
        self.assertEqual(divisao(2, 2), 1)


if __name__ == '__main__':
    main()