def cadastro(nome, idade):
    assert idade >= 18 and idade <= 65, 'Idade do funcionário está entre 18 e 65 anos'
    print(f'{nome} está em idade ativa, pois possui {idade} anos.')

if __name__ == '__main__':
    cadastro('carlos'.title(), 315)

# Carlos está em idade ativa, pois possui 37 anos.
# assert idade >= 18 and idade <= 65, 'Idade do funcionário entre 18 e 65 anos 
# AssertionError: Idade do funcionário está entre 18 e 65 anos