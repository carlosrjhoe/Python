pessoa = {
    'nome': 'carlos',
    'sobrenome': 'conceição',
    'altura': 1.81,
    'endereço':[
        {'rua': 'Av Eraldo Barros de Souza', 'numero': 166}
    ],
}

# quantidade de chave
print(len(pessoa))

# retorna chaves do dicionario
print(pessoa.keys())

# retorna valor da chave
print(pessoa.values())

# valores por default
pessoa.setdefault('idade', None)
print(pessoa)

# copia raza de dicionario
pessoa_01 = pessoa.copy()
pessoa_01['nome'] = 'mayara'
print(pessoa_01)

# pegar pela chave com o get
print(pessoa_01.get('endereço'))

# apagar um item expecifico
pessoa_01.pop('idade')
print(pessoa_01)

# atualizar chave e valor de um dicionario
pessoa_01.update({
    'nome': 'Neto'
})
print(pessoa_01)