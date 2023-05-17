from collections import OrderedDict

dicionario = OrderedDict()
dicionario['a'] = 1
dicionario['b'] = 2
dicionario['c'] = 3
dicionario['d'] = 4
dicionario['e'] = 5

print(dicionario)
print(type(dicionario))

for k, v in dicionario.items():
    print(f'{k} - {v}')
