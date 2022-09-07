nomes = [x for x in input('Digite os nomes, separados por virgulas: ').split(',')]
nomes.sort()

print(','.join(nomes))