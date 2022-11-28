animais = ['cachorro', 'gato', 'cachorro', 'golfinho', 'gato', 'coelho', 'gato']
print(animais)

# print(animais)
# animais = {'carlos': 'dog', 'Mayara': 'cat', 'carlos': 'dog', 'neto': 'goldfish', 'Mayara': 'cat', 'valdenia': 'rabbit', 'Mayara': 'cat'}

while 'gato' in animais:
    """Cada instância de 'gato' é removida até que esse valor não esteja mais na lista"""
    animais.remove('gato')

print(animais)