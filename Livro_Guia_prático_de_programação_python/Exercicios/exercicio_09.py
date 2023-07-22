comidas = []

for comida in range(3):
    comida = input('Qual a sua comida favorita? ')
    comidas.append(comida)
    
print(f'A comida que eu mais gosto é: {comidas[:1]}')
print(f'Minhas duas comidas favoritas são: {comidas[:2]}')
print(f'Dentreas top 3, a comida que eu menos gosto é: {comidas[-1]}')