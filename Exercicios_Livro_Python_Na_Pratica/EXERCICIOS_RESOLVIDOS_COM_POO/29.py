"""29 - Crie um programa que lê um valor de início e um valor de fim, exibindo em tela a contagem dos números dentro desse intervalo.

Feltrin, Fernando. Python na Prática: Aprenda Python Através de Exercícios Comentados (p. 39). Uniorg. Edição do Kindle. """

inicio = int(input('Digite o inicio: '))
fim = int(input('Digite o fim: '))

for i in range(inicio, fim+1):
    print(f'{i}')