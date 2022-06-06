# Listagem 4.6 – Conta de telefone com três faixas de preço

# min = int(input('Quantos minutos você usou no m~es: '))

# if min < 200:
#     preco = 0.20
# else:
#     if min < 400:
#         preco = 0.18
#     else:
#         preco = 0.15

# print(f'Você vai pagar no mês atual R${min*preco:.2f}')

# Listagem 4.8 – Categoria x preço, usando elif

categoria = int(input('digite a categoria do produto: '))
if categoria == 1:
    preco = 10
elif categoria == 2:
    preco = 18
elif categoria == 3:
    preco = 23
elif categoria == 4:
    preco = 26
elif categoria == 5:
    preco = 31
else:
    print('Categoria invalida, digite um valor entre [1 e 5]: ')
    preco = 0
print(f'O preço do produto é R${preco:.2f}')
