
# 1° modo de importar
# import random

# for i in range(5):
#   print(random.randint(1,10))

# 2° modo de importa
# from random import randint

# for i in range(5):
#   print(randint(1,10))

# Encerrando um programa previamente com "sys.exit()"

# import sys
# while True:
#   print('Type exit to exit.')
#   response = input()
#   if response == 'exit':
#     sys.exit()
#   print(f'You typed {response}.')

""" EXERCICIOS
Qual é a diferença entre range(10), range(0, 10) e range(0, 10, 1) em um loop for? """

# for i in range(10):
#   print(i)
# print('##############')
  
# for i in range(1, 10):
#   print(i)
# print('##############')
  
# for i in range(0, 10, 2):
#   print(i)

""" Crie um pequeno programa que mostre os números de 1 a 10 usando um
loop for. Em seguida, crie um programa equivalente que mostre os números
de 1 a 10 usando um loop while """

# for i in range(10):
#   print(i)
# print('##############')

# numero = 0
# while numero <= 10:
#   print(numero)
#   numero += 1

""" Se você tivesse uma função chamada bacon() em um módulo chamado
spam, como você a chamaria após ter importado spam? """

# from spam import bacon