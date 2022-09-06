import random

tamanho = int(input('Digite o tamanho da senha: '))
caracteres = 'abcdefghijklmnopqrstuvxyz!@#%&*^()?'
senha = "".join(random.sample(caracteres, tamanho))

print(senha)