'''PROGRESSÃO ARITIMETICA'''
termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))

pa = termo + (20-1) * razao

for i in range(termo, pa + razao, razao):
    print(i)