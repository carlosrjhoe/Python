"""Exercício 5.4 Modifique o programa anterior para imprimir de 1 até o número
digitado pelo usuário, mas, dessa vez, apenas os números ímpares."""

# fim = int(input('Digite um número: '))
# inicio = 0
# while inicio <= fim:
#     if inicio % 2 != 0:
#         print(inicio)
#     inicio += 1

"""Exercício 5.5 Reescreva o programa anterior para escrever os 10 primeiros múltiplos de 3"""

fim = int(input('Digite um número: '))
inicio = 1
multiplos = []
while inicio <= fim:
    if not len(multiplos) == 10:
        if inicio % 3 == 0:
            multiplos.append(inicio)
            print(inicio)
        inicio += 1
print(multiplos)