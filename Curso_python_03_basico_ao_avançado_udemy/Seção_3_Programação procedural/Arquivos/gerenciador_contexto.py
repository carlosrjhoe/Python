with open('abc.txt', 'w+') as arquivo:
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n')
    arquivo.write('Linha 3\n')
    arquivo.write('Linha 4\n')
    arquivo.write('Outra linha 1\n')
    arquivo.write('Outra linha 2\n')
    
    arquivo.seek(0)
    print(arquivo.read())
    