""" Listagem 6.1 – Uma lista vazia"""
lista = []

""" Listagem 6.2 – Uma lista com três elementos"""
lista = [1, 2, 3]

""" Listagem 6.3 – Acesso a uma lista"""
print(lista)
print(lista[1])
print(lista[2])
print(len(lista))

""" Listagem 6.5 – Cálculo da média"""
notas = [1, 2, 3, 5, 9]
soma = 0
x = 0

while x < len(notas):
    soma += notas[x]
    x += 1
print(f'Média: {soma/len(notas):.2f}')
print(len(notas))