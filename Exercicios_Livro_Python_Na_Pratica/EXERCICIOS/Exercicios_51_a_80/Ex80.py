def inverter_nome(n):
    nome, sobre_nome = n.split()
    return ' '.join([sobre_nome, nome])

pessoa = input('Digite seu nome e sobrenome: ')
pessoa = inverter_nome(pessoa)

print(pessoa)