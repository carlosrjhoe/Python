'''Contagem de 1 até 100'''

'''Importando o modulo sleep da biblioteca time'''
from time import sleep

cont = 0

soma = 0

for i in range(1, 101):
    '''Vai percorrer de 1 a 100'''
    if i % 2 != 0:
        '''Vai verificar se 'i' é impar, se for, será impresso e será somado e contado quantos números impares em dentro da contagem'''
        print(i)
        sleep(0.1)
        cont += 1
        soma += i
print(f'Foi encontrado {cont} números impares.')
print(f'A soma dos números IMPAR é = {soma}')