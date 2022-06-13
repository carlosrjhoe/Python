# lista = []
# print(lista)
# lista.append('a')
# print(lista)
# lista.append('b')
# print(lista)

# lista = []
# while True:
#     n = int(input('Digite um número [0 sai]: '))
#     if n == 0:
#         break
#     lista.append(n)
# x = 0

# while x < len(lista):
#     print(lista[x])
#     x += 1

from re import L


l = []
l = l+[1]
print(l)
l = l+[2]
print(l)
l = l+[3, 4, 5]
print(l)
l.append('a')
print(l)
l.extend(['b', 'c'])
print(l)
l.append(['d', 'f', 'g'])
print(l)
print(l[8])