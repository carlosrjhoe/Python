"""Exercício 4.10 Escreva um programa que calcule o preço a pagar pelo fornecimento
de energia elétrica. Pergunte a quantidade de kWh consumida e o tipo de instalação: 
R para residências, I para indústrias e C para comércios. Calcule o preço a
pagar de acordo com a tabela a seguir"""

qtd_kWh = int(input('Informe a quantidade de kWh consumida: '))
tipo_de_instalacao = input('Informe o tipo de instalação [R(residencia) - I(industrial) - C(comercial)]: ').upper()

if tipo_de_instalacao == 'R':
    if qtd_kWh <= 500:
        preco = 0.40
    else:
        preco = 0.65
elif tipo_de_instalacao == 'C':
    if qtd_kWh <= 1000:
        preco = 0.55
    else:
        preco = 0.60
elif tipo_de_instalacao == 'I':
    if qtd_kWh <= 5000:
        preco = 0.55
    else:
        preco = 0.60
print(f'Quantidade Kwh: {qtd_kWh}Kwh - Valor a pagar: R$ {qtd_kWh*preco:.2f}')