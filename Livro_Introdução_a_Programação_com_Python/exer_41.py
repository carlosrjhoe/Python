"""Exercício 3.11 Faça um programa que solicite o preço de uma mercadoria e o percentual de desconto. Exiba o valor do desconto e o preço a pagar"""

preco = float(input('Digite o preço da mercadoria: '))
percentual = float(input('Digite o percentual do desconto: '))

preco_com_desconto = preco - (preco * percentual / 100)
desconto = preco - preco_com_desconto

print(f'Valor do desconto R${desconto:.2f}')
print(f'Valor do preço com desconto R${preco_com_desconto:.2f}')