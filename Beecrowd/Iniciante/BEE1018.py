valor = int(input())
NOTAS = [100, 50, 20, 10, 5, 2, 1]
cont = 0
print(valor)
for nota in range (len(NOTAS)):
    cont = valor // NOTAS[nota]
    valor %= NOTAS[nota]
    print(f'{cont} nota(s) de R$ {NOTAS[nota]},00')