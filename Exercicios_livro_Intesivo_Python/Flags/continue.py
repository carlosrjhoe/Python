numero_atual = 0
numero_par = []
numero_impar = []

while numero_atual < 10:
    numero_atual += 1
    if numero_atual % 2 == 0:
        numero_par.append(numero_atual)
    else:
        numero_impar.append(numero_atual)
        
print(f'{numero_par}')
print(f'{numero_impar}')