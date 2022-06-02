''' Exercício 3.13 Escreva um programa que converta uma temperatura digitada em
°C em °F. A fórmula para essa conversão é: '''

celsius  = int(input('Digite uma temperatura em [C°]: '))
F = ((9 * celsius) / 5) + 32

print(f'A temperatura de {celsius}c° e igual a {F}f') 