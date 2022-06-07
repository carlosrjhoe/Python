""" Exercício 4.10 Escreva um programa que calcule o preço a pagar pelo fornecimento
de energia elétrica. Pergunte a quantidade de kWh consumida e o tipo de instalação: R para residências, I para indústrias e C para comércios. Calcule o preço a
pagar de acordo com a tabela a seguir """

kwh_cunsumida = int(input('Qual foi o consumo em [kwh]: '))
instalacao = input('Tipo da instação[R- Residencial, I- Industriais, C-Comerciais]: ').upper()

if instalacao == "R":
    if kwh_cunsumida < 500:
        preco = 0.40
    else:
        preco = 0.65
elif instalacao == "I":
    if kwh_cunsumida < 1000:
        preco = 0.55
    else:
        preco = 0.60
elif instalacao == "C":
    if kwh_cunsumida < 5000:
        preco = 0.55
    else:
        preco = 0.60
else:
    print('Codigo errado...')
    preco = 0

print(f'Consumo de {kwh_cunsumida}kwh')
print(f'Preço a pagar pelo consumo R${kwh_cunsumida*preco:.2f}')