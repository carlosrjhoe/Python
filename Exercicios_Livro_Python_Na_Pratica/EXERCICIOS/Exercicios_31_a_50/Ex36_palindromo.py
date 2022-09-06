frase = str(input('Digite uma palavra ou frase: ')).strip().upper()

palavras = frase.split()
caractere = ''.join(palavras)
frase_invertida = ''
for i in range(len(caractere)-1,-1,-1):
    frase_invertida += caractere[i]

if frase_invertida == caractere:
    print('É um palindromo.')
else:
    print('Não é um palindromo.')

'''
upper():
    Retorna uma cópia da string em MAIÚSCULAS.
strip():
    Retorna uma cópia da string com os caracteres iniciais e finais removidos.
'''