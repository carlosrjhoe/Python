"""Exercício 6.8 Modifique o primeiro exemplo (Listagem 6.23) de forma a realizar
a mesma tarefa, mas sem utilizar a variável achou. Dica: observe a condição de
saída do while"""

lista = [1,2,3,4,5,6,7,8,9]
procuro = int(input('Digite o valor que deseja procurar: '))
x = 0
while x < len(lista):
    if lista[x] == procuro:
        break
    x += 1
if x < len(lista):
    print(f'{procuro} achado na posição {x}')
else:
    print(f'{procuro} não foi achado.')