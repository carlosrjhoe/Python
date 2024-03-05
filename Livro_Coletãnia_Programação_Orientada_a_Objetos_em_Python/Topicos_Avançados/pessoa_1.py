class Pessoa:
    pass

pessoa = Pessoa()

dicionario = {
    'nome': 'Carlos',
    'idade': 38,
    'nacionalidade': 'Brasileiro',
}

for chave, valor in dicionario.items():
    setattr(pessoa, chave, valor)

for chave in dicionario.keys():
    print(getattr(pessoa, chave))