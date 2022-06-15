"""Listagem 6.43 – Criação e impressão da lista de compras"""

compras = []
while True:
    produto = input('Produto: ')
    if produto == 'fim':
        break
    quantidade = int(input('Quantidade: '))
    preco = float(input('Preço[R$]: '))
    compras.append([produto, quantidade, preco])
soma = 0.0
for fruta in compras:
    print(f'Fruta: {fruta[0]}\n Quantidade: {fruta[1]}\n Preço: R${fruta[2]:.2f}\n Total: R${fruta[1] * fruta[2]:.2f}')
    soma += fruta[1] * fruta[2]
print(f'Total: R${soma:.2f}')
