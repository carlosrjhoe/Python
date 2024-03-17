numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
nomes = ['carlos', 'mayara', 'neto', 'luna']
dados = [1985, 2024]

"""2 - Crie uma lista e utilize um loop for para percorrer todos os elementos da lista."""
for numero in numeros:
    print(numero)

for nome in nomes:
    print(nome)

"""3 - Utilize um loop for para calcular a soma dos números ímpares de 1 a 10."""
soma = 0
for numero in numeros:
    if numero % 2 == 1:
        soma += numero
print(soma)

"""4 - Utilize um loop for para imprimir os números de 1 a 10 em ordem decrescente."""
for numero in range(len(numeros), 0, -1):
    print(numero)

"""5 - Solicite ao usuário um número e, em seguida, utilize um loop for para imprimir a tabuada desse número, indo de 1 a 10."""
num = int(input('Digite um número de [1 a 10]: '))
for i in range(1, len(numeros)+1):
    print(f'{num} * {i} = {num*i}')

"""6 - Crie uma lista de números e utilize um loop for para calcular a soma de todos os elementos. Utilize um bloco try-except para lidar com possíveis exceções."""


"""7 - Construa um código que calcule a média dos valores em uma lista. Utilize um bloco try-except para lidar com a divisão por zero, caso a lista esteja vazia."""