""" Listagem 6.23 – Pesquisa sequencial"""

lista = [1, 2, 3, 4, 5]
p = int(input('Digite o valor a procurar: '))
achou = False
x = 0
while x < len(lista):
    if lista[x] == p:
        achou = True
        break
    x += 1
if achou:
    print(f'{p} achado na posição {x}')
else:
    print(f'{p} não encontrado.')