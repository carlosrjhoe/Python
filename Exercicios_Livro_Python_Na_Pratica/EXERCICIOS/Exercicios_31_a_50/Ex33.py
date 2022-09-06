'''CONTAGEM REGRESSIVA'''

'''IMPORTANDO UM MODULO (SLEEP) DA BIBLIOTECA TIME'''
from time import sleep

for i in range(20, -1, -1):
    print(i)
    sleep(1)
print('Acabou o tempo!')
