"""14 – Crie uma classe Animal com um método responde( ). Crie duas subclasses, Cão e Gato, que herdam de Animal e sobrescrevem o método responde( ) para retornar "Au Au!" e "Miau!", respectivamente. Crie objetos das subclasses e teste o método responde( ):"""

class Animal:
    def som_animal(self):
        pass

class Cao(Animal):
    def som_animal(self):
        return print('Au Au!')

class Gato(Animal):
    def som_animal(self):
        return print('Miau!')

if __name__ == '__main__':
    cachorro = Cao()
    cachorro.som_animal()
    gato = Gato()
    gato.som_animal()