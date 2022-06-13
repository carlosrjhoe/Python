notas = [0, 0, 0, 0, 0]
soma = 0
x = 0

while x < 5:
    notas[x] = float(input(f'Nota {x}: '))
    soma += notas[x]
    x += 1
x = 0

while x < 5:
    print(f'Nota {x}: {notas[x]:.2f}')
    x += 1

print(f'Média: {soma/x:.2f}')