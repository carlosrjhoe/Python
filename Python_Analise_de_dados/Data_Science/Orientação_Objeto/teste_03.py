""" Conceito de herança """

# Criando a classe Animal - Super-Class
class Animal():
    
    # Método construtor
    def __init__(self) -> None:
        print('Objeto Animal criado')
        
    def identidade(self):
        print('Cachorro')
        
    def comer(self):
        print('Comendo...')
        
# Criando uma class Cachorro(sub-class) da class mãe(Animal)
class Cachorro(Animal):
    
    def __init__(self) -> None:
        Animal.__init__(self)
        
    def identidade(self):
        print('Cachorro')
        
    def latir(self):
        print('Au au!')
        
""" Criando objetos """

tufik = Cachorro()