"""– Supondo que temos um simples carrinho de compras, em formato de lista composta por alguns elementos onde cada elemento da mesma é um dicionário descrevendo um item, crie um mecanismo que retorna ao usuário o valor total do carrinho, seu item mais caro e também seu item mais barato.
"""


def verificarSomaDosProdutos(lista_compras):
    soma = sum([produto['preco'] for produto in lista_compras])
    return soma

def verificarValorMaiorDoProduto(lista_compras):
    produto_maximo = max(lista_compras, key = lambda produto: produto['preco'])
    return produto_maximo

def verificarValorMenorDoProduto(lista_compras):
    produto_minimo = min(lista_compras, key = lambda produto: produto['preco'])
    return produto_minimo

def mostrarDados(lista_compras,verificarSomaDosProdutos,verificarValorMaiorDoProduto,verificarValorMenorDoProduto):
    print(f'Valor da cesta: {verificarSomaDosProdutos(lista_compras):.2f}')
    print(f'Produto mais caro: {verificarValorMaiorDoProduto(lista_compras)["nome"].title()} - R$ {verificarValorMaiorDoProduto(lista_compras)["preco"]:.2f}')
    print(f'Produto mais barato: {verificarValorMenorDoProduto(lista_compras)["nome"].title()} - R$ {verificarValorMenorDoProduto(lista_compras)["preco"]:.2f}')
    return

if __name__ == '__main__':
    lista_compras = [
        {'nome':'feijão', 'preco':9.79},
        {'nome':'arroz', 'preco':3.45},
        {'nome':'carne', 'preco':20.93},
        {'nome':'macarrão', 'preco':2.99},
        {'nome':'biscoito', 'preco':1.09},
        {'nome':'granola', 'preco':13.45},
        {'nome':'galinha', 'preco':25.93},
        {'nome':'Energético', 'preco':10.99}
    ]
    mostrarDados(lista_compras, verificarSomaDosProdutos, verificarValorMaiorDoProduto,verificarValorMenorDoProduto)