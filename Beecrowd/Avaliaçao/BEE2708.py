passageiros = 0
veiculos = 0
while True:
    entrada = input().split()
    if entrada[0] == 'ABEND':
        break
    if entrada[0] == 'SALIDA':
        veiculos += 1
        passageiros += int(entrada[1])
    else:
        veiculos -= 1
        passageiros -= int(entrada[1])
print(passageiros)
print(veiculos)