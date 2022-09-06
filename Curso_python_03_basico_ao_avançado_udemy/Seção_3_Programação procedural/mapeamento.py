from dados import lista_de_precos, lista_de_pessoas, lista_de_numeros

# MAP
# nova_lista = map(lambda x : x * 2, lista_de_numeros)

# LISTACONVERRANGE
# nova_lista = [x * 2 for x in lista_de_numeros]

# print(lista_de_numeros)
# print(list(nova_lista))

# def aumento_de_5_porcento(p):
#     p['preco'] = round(p['preco'] * 1.05, 2)
#     return p

# novos_produtos = map(aumento_de_5_porcento, lista_de_precos)
# for produto in novos_produtos:
#     print(produto)

nomes = map(lambda pessoa: pessoa['nome'], lista_de_pessoas)
for nome in nomes:
    print(f'{nome.title()}')