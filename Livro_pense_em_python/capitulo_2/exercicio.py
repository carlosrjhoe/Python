# x = y = 1
# print(x, y)

"""O volume de uma esfera com raio r é . Qual é o volume de uma esfera com raio 5?"""
# raio = 5

# volume = (4 / 3) * 3.14 * (raio ** 3)
# print(f'O volume de uma esfera com {raio} de raio terá {volume:.3f} metros cúbicos')

"""Suponha que o preço de capa de um livro seja R$ 24,95, mas as livrarias recebem um
desconto de 40%. O transporte custa R$ 3,00 para o primeiro exemplar e 75 centavos
para cada exemplar adicional. Qual é o custo total de atacado para 60 cópias?"""
# copias, preco_capa, desconto, custo_transporte, custo_transporte_adicional = 60, 24.95, 0.40, 3.00, 0.75

# # Calcular preco com  desconto
# preco_desconto = preco_capa * (1 - desconto)

# # Custo custo total dos livros
# custo_total_livros = preco_desconto * copias

# # Custo total do transporte
# custo_total_tranporte = custo_transporte + (custo_transporte_adicional * (copias - 1))

# # Calcular custo total
# custo_total = custo_total_livros + custo_total_tranporte

# print(f'O custo total de atacado para {copias} cópias é R$ {custo_total:.2f}')

""" Se eu sair da minha casa às 6:52 e correr 1 quilômetro a um certo passo (8min15s por
quilômetro), então 3 quilômetros a um passo mais rápido (7min12s por quilômetro) e
1 quilômetro no mesmo passo usado em primeiro lugar, que horas chego em casa
para o café da manhã?"""

# from datetime import datetime, timedelta

# # Dados da saída de casa
# hora_saida = '06:52'
# formato = '%H:%M'

# # Converter hora saída para objeto datetime
# hora_datetime = datetime.strptime(hora_saida, formato)

# # Tempos da corrida transformados de minuto para segundos
# tempo_01 = 8 * 60 + 15
# tempo_02 = 7 * 60 + 12

# # Distância percorrida em cada passo
# distancia_01 = 1
# distancia_02 = 3
# distancia_03 = 1

# # Calcular tempo total gasto em cada passo
# total_passo_01 = distancia_01 * tempo_01
# total_passo_02 = distancia_02 * tempo_02
# total_passo_03 = distancia_03 * tempo_01

# # Calcular tempo total da corrida
# tempo_total_corrida = total_passo_01 + total_passo_02 + total_passo_03

# # Converter o tempo total de segundos para objeto timedelta
# hora_chegada_datetime = timedelta(seconds=tempo_total_corrida)

# # Calcular hora chegada
# hora_chegada_datetime = hora_datetime + hora_chegada_datetime

# # Converter o horário de chegada de volta para string no formato HH:MM
# hora_chegada = hora_chegada_datetime.strftime(formato)

# print(f'Você chegará em casa às {hora_chegada} para o café da manhã')