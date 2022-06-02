''' Exercício 3.9 Escreva um programa que leia a quantidade de dias, horas, minutos
e segundos do usuário. Calcule o total em segundos '''

dias = int(input('Digite quantidade de dias: '))
horas = int(input('Digite quantidade de horas: '))
minutos = int(input('Digite quantidade de minutos: '))
segundos = int(input('Digite quantidade de segundos: '))

dias_em_segundos = dias * 86400
horas_em_segundos = horas * 3600
minutos_em_segundos = minutos * 60
total = dias_em_segundos + horas_em_segundos + minutos_em_segundos + segundos

print(f'Total em segundos: {total}s')