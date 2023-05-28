'''Crie um mecanismo que gera um número pseudorrandômico, no intervalo entre 0 e 1, exibindo tal número em tela com 5 casas decimais após a vírgula.
'''

import random

def gerar_numero_pseudorrandomico(numero):
    random.seed(numero)
    num = random.random() # Gera um número aleatório dentro do intervalo entre 0 e 1.
    print(f'{num:.5}') # Exibir os primeiros 5 números após a vírgula.
    return

if __name__ == '__main__':
    gerar_numero_pseudorrandomico(42)