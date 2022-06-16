""" Listagem 6.52 – Dicionário com listas"""

estoque = {
    'tomate': [1000, 2.30],
    'alface': [500, 0.45],
    'batata': [2001, 1.20],
    'feijão': [100, 1.50],
}
# print(estoque)

""" Listagem 6.53 – Exemplo de dicionário com estoque e operações de venda"""

venda = [ ['tomate', 5], ['batata', 10], ['alface', 5] ]
total = 0
for operacao in venda:
    produto, quantidade = operacao
    preco = estoque[produto][1]
    custo = preco * quantidade
    print(f'{produto}: {quantidade} x {preco:.2f} = R${custo:.2f}')
    estoque[produto][0] -= quantidade
    total += custo
print(f'Custo total: R${total:.2f}')
print('Estoque:\n')
for chave, dados in estoque.items():
    print(f'Descrição: {chave}')
    print(f'Quantidade: {dados[0]}')
    print(f'Preço: R${dados[1]:.2f}')