"""Exercício 3.9 Escreva um programa que leia a quantidade de dias, horas, minutos
e segundos do usuário. Calcule o total em segundos."""

dias = int(input('Digite a quantidade de dias: '))
horas = int(input('Digite a quantidade de horas: '))
minutos = int(input('Digite a quantidade de minutos: '))
dias_segundos = dias * 86400
horas_segundos = horas * 3600
minutos_segundos = minutos * 60
total_segundos = dias_segundos + horas_segundos + minutos_segundos
print(f'Total: {total_segundos}s')