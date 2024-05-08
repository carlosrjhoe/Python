url = 'pagina?argumentos'

# index = url.find('=')
# subString = url[index + 1:]
# print(subString)

# CELULAR = '(81)99541-9951'
# INICIO = CELULAR.find('(')+1
# FINAL = CELULAR.find(')')
# codigo_cidade = CELULAR[INICIO:FINAL]
# print(codigo_cidade)

indice = url.find('?')
print(url[indice+1:])