primeira = []
segunda = []

while True:
    primeira_lista = int(input('Digite um valor para a primeira lista [0 para terminar]: '))
    if primeira_lista == 0:
        break
    primeira.append(primeira_lista)
    
while True:
    segunda_lista = int(input('Digite um numero para segunda lista [0 para sair]: '))
    if segunda_lista == 0:
        break
    segunda.append(segunda_lista)

terceira = primeira[:]
terceira.extend(segunda)

x = 0
while x < len(terceira):
    print(f'{x}: {terceira[x]}')
    x += 1