"""bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

print(bicycles[0].title())
print(bicycles[2].title())
print(bicycles[-1])"""

nomes = ['carlos', 'mayara', 'neto', 'luna']
print(nomes)
nomes.append('rosiclé')
print(nomes)
nomes.insert(0, 'Lúcinha')
print(nomes)
del nomes[5]
print(nomes)

nomes_retirados = nomes.pop()
print(nomes)
print(nomes_retirados)
nomes_retirados = nomes.pop()
print(nomes)
print(nomes_retirados)