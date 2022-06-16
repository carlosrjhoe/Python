""" Listagem 6.45 – Criação de um dicionário"""

tabela = {
    'Alface': 0.45,
    'Batata': 1.20,
    'Tomate': 2.30,
    'Feijão': 1.50
}
# print(tabela)
# tabela['Cebola'] = 1.20
# print(tabela)

# print('manga' in tabela)
# print('Cebola' in tabela)

# print(tabela.keys())
# print(tabela.values())

""" Listagem 6.50 – Obtenção do preço com um dicionário"""

while True:
    produto = input("Digite o nome do produto['fim' para terminar]: ")
    if produto == 'fim':
        break
    elif produto in tabela:
        print(f'Produto: R${tabela[produto]:.2f}')
    else:
        print('Produto não encontrado!')