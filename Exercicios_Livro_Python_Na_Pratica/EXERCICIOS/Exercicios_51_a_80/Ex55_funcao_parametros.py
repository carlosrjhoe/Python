def boas_vindas(nome, sobrenome):
    return f'Bem vindo(a) {nome} {sobrenome}'

nome = input('Digite o nome: ')
sobrenome = input('Digite o sobre nome: ')

print(boas_vindas(nome, sobrenome))