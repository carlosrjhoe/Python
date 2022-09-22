from dados import lista_de_precos, lista_de_pessoas, lista_de_numeros

# MAP
# nova_lista = map(lambda x : x * 2, lista_de_numeros)
# print(lista_de_numeros)
# print(list(nova_lista))

# LISTACONVERRANGE
# nova_lista = [x * 2 for x in lista_de_numeros]
# print(nova_lista)

# print(lista_de_numeros)
# print(list(nova_lista))

# def aumento_de_5_porcento(p):
#     p['preco'] = round(p['preco'] * 1.05, 2)
#     return p


# novos_produtos = map(aumento_de_5_porcento, lista_de_precos)
# for produto in novos_produtos:
#     print(produto)


def aumentar_idade(p):
    p['nova_idade'] = round(p['idade'] * 1.2)
    return p
    
pessoas = map(aumentar_idade, lista_de_pessoas)
for pessoa in pessoas:
    print(f'Meu nome é: {pessoa["nome"].title()}, e eu tenho {pessoa["idade"]} anos de idade.')