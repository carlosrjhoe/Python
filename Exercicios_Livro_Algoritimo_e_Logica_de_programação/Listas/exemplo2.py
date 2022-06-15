"""Listagem 6.34 – Cópia de elementos para outras listas"""
v = [1,2,3,4,5]
pares = []
impares = []
for i in v:
    if i % 2 == 0:
        pares.append(i)
    else:
        impares.append(i)
print(f'Pares: {pares}')
print(f'impares: {impares}')