arquivo = open('palavras.txt', 'w')

arquivo.write('Banana')
arquivo.write('Melancia')
arquivo.write('Manga')

arquivo.close()

arquivo = open('palavras.txt', 'r')
frutas = []
for fruta in arquivo:
    fruta = fruta.strip()
    frutas.append(fruta)
    print(f'{frutas}')
