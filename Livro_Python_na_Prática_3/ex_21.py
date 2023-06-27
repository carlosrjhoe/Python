"""21 - Utilizando a biblioteca random, crie um script que gere senhas seguras contendo letras maiúsculas, minúsculas, números e caracteres especiais. Permita ao usuário escolher o tamanho da senha e a quantidade de senhas geradas:"""
import string
import random

def gerar_senha(tamanho):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(caracteres) for _ in range(tamanho))

def main():
    tamanho_senha = int(input('Digite o tamanho desejado para a senha: '))
    quantidade_senhas = int(input('Digite a quantidade de senhas que deseja gerar: '))

    for _ in range(quantidade_senhas):
        print(f'Senha gerada: {gerar_senha(tamanho_senha)}')

if __name__ == '__main__':
    main()

    # >>> Digite o tamanho desejado para a senha: 10
    # >>> Digite a quantidade de senhas que deseja gerar: 5
    # >>> Senha gerada: tTo4dUassT
    # >>> Senha gerada: yVVB)F|7{M
    # >>> Senha gerada: _ieg.[=>1[
    # >>> Senha gerada: t:<sG<{CGk
    # >>> Senha gerada: `&0)6J(Lt>