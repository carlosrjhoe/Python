tupla = (1, 2, 3)
cunjunto = {4, 5, 6}

dict1 = {'um': 1, 'dois': 2}
dict2 = {'tres': 3, 'quatro': 4}

lista = [*tupla, *cunjunto]
dicionarios = {**dict1, **dict2}

print(lista)
print(dicionarios)