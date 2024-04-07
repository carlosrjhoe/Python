"""Altere o programa anterior para exibir os resultados no mesmo formato de uma tabuada: 2x1 = 2, 2x2=4, ..."""

# num = int(input('tabuada de: '))
# x = 1
# while x <= 10:
#     resultado = x + num
#     print(f'{x} + {num} = {resultado}')
#     x += 1

"""Exercício 5.7 Modifique o programa anterior de forma que o usuário também
digite o início e o fim da tabuada, em vez de começar com 1 e 10"""

num = int(input('Tabuada de: '))
inicio = int(input('Iniando em: '))
fim = int(input('termina em: '))
x = 1
while x <= fim:
    if x >= inicio and x <= fim:
        resultado = x + num
        if inicio <= fim:
            print(f'{x} + {num} = {resultado}')
    x += 1