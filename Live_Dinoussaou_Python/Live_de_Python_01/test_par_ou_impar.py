# Importando a biblioteca de testes
from unittest import TestCase, main

def par(valor):
    # Função onde me retor "Verdadeiro" se o valor for par
    try:
        return True if valor % 2 == 0 else False
    except TypeError:
        return False
    
def impar(valor):
    # Função onde me retor "Verdadeiro" se o valor for impar
    return True if valor % 2 != 0 else False

# Case de testes
class Testes(TestCase):
    def test_par(self):
        self.assertEqual(par(2), True)
        
    def test_impar(self):
        self.assertEqual(impar(3), True)
        
        
if __name__ == '__main__':
    main()