carlos = {'nome': 'carlos', 'idade': 37, 'formacao': ['Analista de Sistemas', 'Técnico em mecânica']}

# print(type(carlos))
# print(len(carlos))

"""Consultando chaves/valores de um dicionário"""
# print(carlos.get('nome'))
# print(carlos.get('idade'))
# print(carlos.get('formacao'))

"""Consultando as chaves de um dicionário"""
print(carlos.keys())

"""Consultando as values de um dicionário"""
print(carlos.values())

"""Mostrando todas chaves e valores de um dicionário"""
print(carlos.items())

"""Manipulando dados de um dicionário"""
carlos['nacionalidade'] = 'brasileiro'
print(carlos.items())

"""Adicionando novos dados a um dicionário"""
carlos['formacao'].append('vigilante')
print(carlos.items())