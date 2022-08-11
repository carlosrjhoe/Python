# palavra = 'USANDO BREAK COM LAÇO'
# print('#'*len(palavra))
# print(f'{(palavra.center(len(palavra)))}')
# print('#'*len(palavra))

# while True:
#     cidade = input('Digite o nome de uma cidade que você visitou: \n[digite "sair" para terminar] ')
#     if cidade == 'sair':
#         break
#     else:
#         print(f'Eu adoraria ir para {cidade.title()}')


palavra = 'USANDO CONTINUE EM UM LAÇO'
print('#'*len(palavra))
print(f'{(palavra.center(len(palavra)))}')
print('#'*len(palavra))

numero_atual = 0
numero_pares = [] # Lista vazia de números pares
numeros_impares = [] # Lista vazia de números impares

while numero_atual < 10:
    numero_atual += 1
    # Se o resto da divisão for "0" o número é par
    if numero_atual % 2 == 0:
        # Adicionar o numero atual em lista de numeros páres
        numero_pares.append(numero_atual)
    else:
        #  Se o resto da divisão for diferente de "0" o número é impar.
        # Adicionar o número atual em lista de números impares
        numeros_impares.append(numero_atual)
        continue
print(f'{numero_pares}\n{numeros_impares}')