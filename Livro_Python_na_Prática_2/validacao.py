"""Crie um simples mecanismo validador que recebe do usuário um texto qualquer e retorna ao mesmo se tal texto pertence ou não a uma frase pré-definida."""

def procurar_palavra(texto, pesquisa):
    if (texto.find(pesquisa) == -1):
        print(f'Palavra {pesquisa} não encontrada no texto de origem.')
    else:
        print(f'Palavra {pesquisa} é uma das palavras do texto de origem.')


if __name__ == '__main__':
    texto = 'Python é uma excelente linguagem de programação!!!'
    pesquisa = input('Digite uma palvra a ser pesquisada: ')
    procurar_palavra(texto, pesquisa)