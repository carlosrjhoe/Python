import inspect

class Calculadora:
    def soma(self, num_1, num_2):
        resultado = num_1 + num_2
        print(resultado)

minha_soma = Calculadora()
minha_soma.soma(12, 35)
print(minha_soma.soma.__class__)
print(minha_soma.soma.__func__)

valida_funcao = inspect.isfunction(minha_soma.soma)
print(valida_funcao)
valida_metodo = inspect.ismethod(minha_soma.soma)
print(valida_metodo)