from dados import lista_de_precos, lista_de_pessoas, lista_de_numeros

lista_menor_que_5 = filter(lambda x: x['preco'] > 10, lista_de_precos)
lista_maior_que_5 = filter(lambda x: x['preco'] < 3, lista_de_precos)

# LISTACONVERRANGE
# lista_maior_que_5 = [x for x in lista_de_numeros if x > 5]
# lista_menor_que_5 = [x for x in lista_de_numeros if x < 5]

# print(lista_de_precos)
for produto in lista_maior_que_5:
    print(produto)

for produto in lista_menor_que_5:
    print(produto)