"""Exercício 5.5 Reescreva o programa anterior para escrever os 10 primeiros múltiplos de 3"""

from cgi import print_form


fim = int(input('Digite o último número a sem imprimido: '))
x = 0
multiplos_de_tres = []
# Lista vazia
while x <= fim:
    if x % 3 == 0:
        multiplos_de_tres.append(x)
        # Adicionando números multiplos de 3 na lista vazia
    x += 1
print(multiplos_de_tres)
