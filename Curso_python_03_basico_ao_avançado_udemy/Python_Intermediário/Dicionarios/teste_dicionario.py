pessoa = {
    'nome': 'carlos',
    'sobrenome': 'conceição',
    'idade': 37,
    'altura': 1.81,
    'endereço':[
        {'rua': 'Av Eraldo Barros de Souza', 'numero': 166}
    ],
}


# print(pessoa, type(pessoa))
for chave in pessoa:
    print(f'{chave}: {pessoa[chave]}')