''' Exercício 3.11 Faça um programa que solicite o preço de uma mercadoria e o percentual de desconto. Exiba o valor do desconto e o preço a pagar '''

preco = float(input('Digite o valor da mercadoria: '))
porcento = int(input('Digite o valor do desconto[%]: '))
desconto = preco * porcento / 100
novo_preco = preco - desconto

print(f'Valor do desconto = R${desconto:.2f}')
print(f'Valor da mercadoria com o desconto = R${novo_preco:.2f}')