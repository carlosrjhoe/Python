# Criando uma class
class Circulo():
    
    # Valor de PI é constante
    pi = 3.14
    
    # Quando um objeto dessa classe for criado, este método será executado e o valor default do raio será 5.
    def __init__(self, raio=5) -> None:
        self.raio = raio
        
    # Este método calcula a área, Self utiliza os atributos deste mesmo objeto.add()
    def area(self):
        return (self.raio * self.raio) * Circulo.pi
    
    # Método para gerar um novo raio
    def setRaio(self, novo_raio):
        self.raio = novo_raio
        
    # Método para obter o raio do círculo
    def getRaio(self):
        return self.raio

# Criando um objeto com o nome circ. Uma instância da classe Circulo 
circ = Circulo()

# Executando e imprindo um método da classe Circulo
print(f'O raio é: {circ.getRaio()}')


# Imprimindo o método da area
print(f'A área é: {circ.area()}')
