"""25 - Peça para que o usuário digite um número, em seguida exiba em tela uma mensagem dizendo se tal número     é PAR ou se é ÍMPAR:"""

def pergunta():
    num = int(input('Digite um número: '))

    if num % 2 == 0:
        print(f'PAR')
    else:
        print(f'IMPAR')


if __name__ == '__main__':
    pergunta()