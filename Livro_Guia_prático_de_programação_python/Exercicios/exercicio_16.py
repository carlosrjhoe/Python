notas = []

for nota in range(4):
    nota = float(input('Digite o valor da nota? '))
    notas.append(nota)

media = sum(notas) / len(notas)
print(media)

if media < 7:
    print('reprovado!')
elif media > 7 and  media < 9.9:
    print('Aprovado')
elif media == 10:
    print('Aprovado com louvor!')
    
    