from dados import lista_de_precos, lista_de_numeros, lista_de_pessoas
from functools import reduce

# FORMA NORMAL DE ACUMULAR OS NUMEROS DE UMA LISTA

# acumulador = 0
# for item in lista_de_numeros:
#     acumulador += item
# print(lista_de_numeros)
# print(acumulador)    

# REDUCE

# soma_de_lista = reduce(lambda acumulador, item: item + acumulador, lista_de_numeros, 0)
# print(soma_de_lista)

# soma_valor_produtos = reduce(lambda acumulador, preco: preco['preco'] + acumulador, lista_de_precos, 0)
# print(f'Valor total: R${soma_valor_produtos:.2f}')

soma_de_idade = reduce(lambda acumulador, idade: idade['idade'] + acumulador, lista_de_pessoas, 0)
print(lista_de_numeros)
print(soma_de_idade / len(lista_de_pessoas))