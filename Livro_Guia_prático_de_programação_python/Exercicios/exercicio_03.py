'''
    Um comerciante vendeu 30 unidades de um produto que custa R$ 5.
    Qual foi o valor total das vendas?
'''

valor_total = lambda unidade, produto: unidade * produto
print(f'Valor total das vendas: R${valor_total(30, 5):.2f}')