notas = []

for nota in range(4):
    nota = float(input('Digite sua nota: '))
    notas.append(nota)
    
print(len(notas))
print(sum(notas))
print(f'Média: {sum(notas)/len(notas)}')
