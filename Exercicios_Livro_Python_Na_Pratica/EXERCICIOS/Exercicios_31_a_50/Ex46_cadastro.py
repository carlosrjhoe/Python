from multiprocessing import Value


cadastro_pessoa = {
    'Sexo': 'Masculino',
    'Idade': 36,
    'Nacionalidade': 'Brasil',
    'Estado Civil': 'Casado',
    'Escolaridade': ['Superior', 'Doutorado'],
    'Ocupação': 'Estudante',
    'Renda': '2000.00 - 299999'
}

print(type(cadastro_pessoa))
print(cadastro_pessoa)