numero = int(input('Digite um número: '))
dicionario = {}

for i in range(1, numero+1):
    dicionario[i] = i*i
    
print(dicionario)