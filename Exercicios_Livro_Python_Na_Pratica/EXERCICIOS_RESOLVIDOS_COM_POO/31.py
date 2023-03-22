"""31 - Crie um programa que realiza a Progressão Aritmética de 20 elementos, com primeiro termo e razão definidos pelo usuário:

Feltrin, Fernando. Python na Prática: Aprenda Python Através de Exercícios Comentados (p. 42). Uniorg. Edição do Kindle. """

termo = int(input('Digite o termo: '))
razao = int(input('Digite razão: '))
pa = termo + (20-1)*razao

for i in range(termo, pa+razao, razao):
    print(f'{i}')