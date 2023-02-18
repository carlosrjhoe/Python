import unitest

def soma(x):
    return x + 1

class MyTest(unitest.TestCase):
    
    def teste_se_vai_somar(self):
        self.assertEqual(soma(3), 4)