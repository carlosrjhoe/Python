"""Exercício 3.14 Escreva um programa que pergunte a quantidade de km percorridos
por um carro alugado pelo usuário, assim como a quantidade de dias pelos quais
o carro foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60 por
dia e R$ 0,15 por km rodado"""

qtd_km = float(input('Digite a quantidade de km rodado: '))
dias = int(input('Digite a quantidade de dias de aluguel: '))

preco_km_rodado = qtd_km * 0.15
preco_por_dias_rodados = dias * 60
total_do_aluguel = preco_km_rodado + preco_por_dias_rodados

print(f'Preço a total do aluguém do veículo: R$ {total_do_aluguel:.2f}')
