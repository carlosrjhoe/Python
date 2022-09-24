arquivo = open('palavras.txt', 'w')

arquivo.write('Banana\n')
arquivo.write('Melancia\n')
arquivo.write('Manga\n')

arquivo.close()

arquivo = open('palavras.txt', 'r')
frutas = []
for fruta in arquivo:
    fruta = fruta.strip()
    frutas.append(fruta)

for i in frutas:
    print(f'{i}')
