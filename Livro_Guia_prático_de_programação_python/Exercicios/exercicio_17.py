vogais = ['a', 'e', 'i', 'o', 'u']
consoantes = ['b', 'c', 'd', 'f', 'g','h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']

letra = input('Digite uma letra: ')
if letra.lower() in vogais: 
    print('É vogal!')
elif letra.lower() in consoantes:
    print('Não é vogal!')
else:
    print('Valor inválido!')