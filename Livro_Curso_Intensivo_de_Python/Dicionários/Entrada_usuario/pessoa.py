def caracteristicas(primeiro_nome, segundo_nome, idade=''):
    """Devolve um dicionário com informações sobre uma pessoa."""
    pessoa = {'Primeiro': primeiro_nome, 'Segundo': segundo_nome}
    if idade:
        pessoa['idade'] = idade
    return pessoa

print(type(caracteristicas('carlos', 'roberto')))
print(caracteristicas('carlos', 'roberto'))
print(caracteristicas('mayara', 'ramos', 37))
print(caracteristicas('neto', 'conceicao', 6))
print(caracteristicas('luna', 'ramos', 4))