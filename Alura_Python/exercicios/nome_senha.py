DADOS = {'nome': 'carlos', 'senha': 12345}

def verificacao():
    nome = input('Digite seu nome: ')
    senha = int(input('Digite sua senha: '))

    if nome != DADOS['nome'] and senha != DADOS['senha']:
        print('Nome e senha inválidos')
    elif nome == DADOS['nome'] and senha == DADOS['senha']:
        print('Nome e senha válidos')

def main():
    verificacao()

if __name__ == "__main__":
    main()