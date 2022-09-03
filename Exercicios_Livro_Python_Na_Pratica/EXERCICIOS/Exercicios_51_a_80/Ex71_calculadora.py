class Calculadora:
    
    def soma(self, numero1, numero2):
        return numero1 + numero2
    
    def subtracao(self, numero1, numero2):
        return numero1 - numero2
    
    def multiplicacao(self, numero1, numero2):
        return numero1 * numero2
    
    def divisao(self, numero1, numero2):
        return numero1 / numero2
    
    
calculo = Calculadora()

print(calculo.soma(5,3))
print(calculo.subtracao(10,3))
print(calculo.multiplicacao(7,9))
print(calculo.divisao(20,4))

