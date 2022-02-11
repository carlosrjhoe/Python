frase = str(input('Digite uma palavra ou frase: ')).strip().upper()
'''
upper():
    Retorna uma cópia da string em MAIÚSCULAS.
strip():
    Retorna uma cópia da string com os caracteres iniciais e finais removidos.
'''

palavras = frase.split()
caractere = ".join(palavras)fraseinvertida="
for i in range(len(caractere)-1,-1,-1):
    fraseinvertida += caractere
print(caractere)