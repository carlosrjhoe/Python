from unittest import TestCase, main

def par(valor):
    return True if valor % 2 == 0 else False

def impar(valor):
    return True if valor % 2 != 0 else False


class Testes(TestCase):
    def test_par(self):
        self.assertEqual(par(2), True)
        
    def test_impar(self):
        self.assertEqual(impar(3), True)
        
        
if __name__ == '__main__':
    main()