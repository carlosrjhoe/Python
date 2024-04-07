"""Altere o programa anterior para exibir os resultados no mesmo formato de uma tabuada: 2x1 = 2, 2x2=4, ..."""

# num = int(input('tabuada de: '))
# x = 1
# while x <= 10:
#     resultado = x + num
#     print(f'{x} + {num} = {resultado}')
#     x += 1

"""Exercício 5.7 Modifique o programa anterior de forma que o usuário também
digite o início e o fim da tabuada, em vez de começar com 1 e 10"""

# num = int(input('Tabuada de: '))
# inicio = int(input('Iniando em: '))
# fim = int(input('termina em: '))
# x = 1
# while x <= fim:
#     if x >= inicio and x <= fim:
#         resultado = x + num
#         if inicio <= fim:
#             print(f'{x} + {num} = {resultado}')
#     x += 1

"""Exercício 5.8 Escreva um programa que leia dois números. Imprima o resultado da
multiplicação do primeiro pelo segundo. Utilize apenas os operadores de soma e
subtração para calcular o resultado. Lembre-se de que podemos entender a multiplicação de dois 
números como somas sucessivas de um deles. Assim, 4 × 5 = 5 + 5 + 5 + 5 = 4 + 4 + 4 + 4 + 4"""

# num1 = int(input("Digite o primeiro número: "))
# num2 = int(input("Digite o segundo número: "))
# x = 1
# r = 0

# while x <= num2:
#     r += num1
#     x += 1
# print(f'{num1} x {num2} = {r}')

"""Exercício 5.9 Escreva um programa que leia dois números. Imprima a divisão
inteira do primeiro pelo segundo, assim como o resto da divisão. Utilize apenas
os operadores de soma e subtração para calcular o resultado. Lembre-se de que
podemos entender o quociente da divisão de dois números como a quantidade
de vezes que podemos retirar o divisor do dividendo. Logo, 20 ÷ 4 = 5, uma vez
que podemos subtrair 4 cinco vezes de 20"""

def divisao_inteira_e_resto(dividendo, divisor):
    quociente = 0
    resto = dividendo
    
    while resto >= divisor:
        resto -= divisor
        quociente += 1
    
    return quociente, resto

def main():
    num1 = int(input("Digite o dividendo: "))
    num2 = int(input("Digite o divisor: "))

    quociente, resto = divisao_inteira_e_resto(num1, num2)
    print("A divisão inteira é:", quociente)
    print("O resto da divisão é:", resto)

main()