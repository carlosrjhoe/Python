"""Exercício 3.13 Escreva um programa que converta uma temperatura digitada em
°C em °F."""

temperatura = int(input('Digite a temperatura em graus celsius: '))

F = ((9 * temperatura) / 5) + 32

print(f'Temperatura em C° convertida {F}°F')