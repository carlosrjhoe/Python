"""Introdução à List comprehension em Python"""

# List comprehension é uma forma rápida para criar listas
# a partir de iteráveis.
# print(list(range(10)))
# lista = []
# for numero in range(20):
#     if numero % 2 == 1:
#         lista.append(numero)
# print(lista)
#
# lista = [numero * 2 for numero in range(20)]
# print(lista)

# Dicionários comprehension em Python

pessoas = {
    'Nome': 'Carlos Roberto',
    'Idade': 39,
    'Profissao': 'Encarregado'
}

# for chave, valor in Pessoas.items():
#     print(f'{chave}: {valor}')

dc = {
    chave: valor.upper()
    if isinstance(valor, str) else valor
    for chave, valor in pessoas.items()
}

print(dc)
