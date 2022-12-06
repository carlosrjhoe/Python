from Calculadora_01 import Calculadora

print(Calculadora.soma(1, 2))

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)