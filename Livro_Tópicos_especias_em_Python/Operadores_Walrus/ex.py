carrinho = []

def adicionar_no_carrinho():
    print('Quando quiser, digite [sair] para encerrar o programa.')
    while (objeto := input('Digite um objeto: ')) != 'sair':
        carrinho.append(objeto.title())
    print(f'Lista do carrinho: {carrinho}')

if __name__ == '__main__':
    adicionar_no_carrinho()
    
# Quando quiser, digite [sair] para encerrar o programa.
# Digite um objeto: lápis
# Digite um objeto: caneta
# Digite um objeto: corracha
# Digite um objeto: caderno
# Digite um objeto: livro de python
# Digite um objeto: sair
# ['Lápis', 'Caneta', 'Corracha', 'Caderno', 'Livro De Python']