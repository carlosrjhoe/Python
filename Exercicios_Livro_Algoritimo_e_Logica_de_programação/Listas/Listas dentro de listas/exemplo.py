"""Listagem 6.38 – Listas com strings, acessando letras"""

s = ['macâs', 'banana', 'pera', 'uva']
# print(s[0][0])
# print(s[1][1])
# print(s[2][2])
# print(s[3][2])
# print(s[1][3])

"""Listagem 6.39 – Impressão de uma lista de strings, letra a letra"""

# for fruta in s:
#     for letra in s:
#         print(letra)
        
""" Listagem 6.40 – Listas com elementos de tipos diferentes"""

produto1 = ['Macâ', 10, 1.30]
produto2 = ['Pera', 5, 2.75]
produto3 = ['Kiwi', 4, 3.98]
compras = produto1, produto2, produto3
for fruta in compras:
    print('-=' * 7)
    print(f'Produto: {fruta[0]}')
    print(f'Quantidade: {fruta[1]}')
    print(f'Preço: R${fruta[2]:.2f}')
    print(f'Total: R${fruta[2] * fruta[1]:.2f}')