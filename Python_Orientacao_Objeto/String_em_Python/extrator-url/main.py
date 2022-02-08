url = 'bytebank.com/cambio?moedaOrigem=real'
print(url)

# Separa base e os parâmetros
indice_interrogacao = url.find('?')
url_base = url[0:indice_interrogacao]
url_parametros = url[indice_interrogacao+1:36]
print(url_parametros)

# Busca o valor de um parâmetro
paramentro_de_busca = 'moedaOrigem'
indice_paramentro = url_parametros.find(paramentro_de_busca)
indice_valor = indice_paramentro + len(paramentro_de_busca) + 1
indice_e_comercial = url_parametros.find('&', indice_valor)

if indice_e_comercial == -1:
    valor = url_parametros[indice_valor:]
else:
    valor = url_parametros[indice_valor:indice_e_comercial]
    
print(valor)

'''
METODO FIND():
    Determina se a string str ocorre em string, ou em uma substring de string se o índice inicial beg e o índice final end forem fornecidos.

    Sintaxe
    url.find('?')
    
METODO LEN()
    A função retorna o número de itens em um objeto.
    Quando o objeto é uma string, a len()função retorna o número de caracteres na string.
    
    Sintaxe
    len(object)
'''