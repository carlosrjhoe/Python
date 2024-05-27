"""Quantos segundos há em 42 minutos e 42 segundos?"""
# minutos, segundo = 42, 42

# # Converter minutos em segundos
# segundos = minutos * 60

# # Retorno dos minutos transformados em segundos somados aos segundos restantes
# print(f'Total de segundos em {minutos} minutos e {segundo} segundos é de: {segundos + segundo} segundos')

"""2. Quantas milhas há em 10 quilômetros? Dica: uma milha equivale a 1,61 quilômetro"""
# quilometro, milha = 10, 0.61

# # Converter quilometros em milhas
# milhas = quilometro * milha

# # Retorno de quilomentros transformados em milhas
# print(f'{quilometro} Quilomentos é igual a {milhas:.3f} milhas.')

"""Se você correr 10 quilômetros em 42 minutos e 42 segundos, qual é o seu passo
médio (tempo por milha em minutos e segundos)?"""
kilometros, minutos, segundos, milha = 10, 42, 42, 1.60934

# Converter distancia de km para milhas
milhas = kilometros * milha

# Converter o tempo total para segundos
total_segundos = (minutos * 60) + segundos

# Tempo médio por milhas em segundos
tempo_medio_milhas = total_segundos / milhas

# Converter tempo médio de milhas por minuto
passo_minuto = int(tempo_medio_milhas // 60)

# Converter tempo médio de milhas por hora
passo_hora = minutos / 60 + segundos / 3600

# Converter tempo médio de milhas por segundos
passo_segundos = int(tempo_medio_milhas % 60)

# Retorno de tempo por milha em minutos e segundos
print(f'Passo médio é {passo_minuto} minutos e {passo_segundos} segundos por milha.')
print(f'Velocidade média é {passo_hora:.2f} milhas por hora')