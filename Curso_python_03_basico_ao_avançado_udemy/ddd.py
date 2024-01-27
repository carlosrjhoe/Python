estados = {
    '61': 'Brasilia',
    '71': 'Salvador',
    '11': 'São paulo',
    '21': 'Rio de Janeiro',
    '32': 'Juiz de Fora',
    '19': 'Campinas',
    '27': 'Vitoria',
    '31': 'Belo Horizonte',
}

ddd = input()
print(estados.get(ddd, 'DDD não cadastrado'))