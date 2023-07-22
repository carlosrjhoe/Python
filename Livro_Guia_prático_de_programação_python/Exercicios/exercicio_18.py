media = []

for nota in range(2):
    nota = float(input('Digite uma nota: '))
    media.append(nota)
    
media = sum(media) / len(media)

if media < 6.9:
    print(f'Media: {media}\nConceito D.\nReprovado')
elif media >= 6.9 and media <= 7.5:
    print(f'Media: {media}\nConceito C.\nAprovado')
elif media > 7.5 and media < 9.0:
    print(f'Media: {media}\nConceito B.\nAprovado')
elif media > 9.0:
    print(f'Media: {media}\nConceito A.\nAprovado')
    
    