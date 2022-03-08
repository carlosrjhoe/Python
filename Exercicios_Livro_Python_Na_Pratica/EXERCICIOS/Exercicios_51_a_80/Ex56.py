def boas_vindas(nome, nacionalidade='Brasileiro'):
    return f'Bem vindo(a) {nome} {nacionalidade}'

nome = input('Digite o nome: ')
nacionalidade = input('Digite sua nacionalidade: ')

print(boas_vindas(nome)