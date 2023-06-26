"""11 – Crie um decorador que calcule e imprima o tempo de execução da função decorada. Aplique o decorador a uma função que demore algum tempo para ser executada, como uma função que calcule o fatorial de um número:"""

from time import time

def tempo_decorador(funcao):
    def msg(*args, **kwargs):
        inicio = time()
        resultado = funcao(*args, **kwargs)
        fim = time()
        print(f'Tempo de execução: {fim - inicio}')
        return resultado
    return msg

@tempo_decorador
def fatorial(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

if __name__ == '__main__':
    print(fatorial(10))