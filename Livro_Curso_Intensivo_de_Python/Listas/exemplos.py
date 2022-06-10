"""bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

print(bicycles[0].title())
print(bicycles[2].title())
print(bicycles[-1])"""

nomes = ['carlos', 'mayara', 'neto', 'luna']
print(nomes)
nomes.append('rosiclé')
print(nomes)
nomes.insert(0, 'lúcinha')
print(nomes)
del nomes[5]
print(nomes)

nomes_retirados = nomes.pop()
print(nomes)
print(nomes_retirados)
nomes_retirados = nomes.pop()
print(nomes)
print(nomes_retirados)
nomes.remove('mayara')
print(nomes)
nomes.append('mayara')
print(nomes)
nomes.insert(0, 'neto')
print(nomes)
nomes.insert(2, 'luna')
nomes.insert(3, 'rosiclé')
print(nomes)
nomes.sort()
print(nomes)
nomes.reverse()
print(nomes)
print(len(nomes))