''' Exercício 3.14 Escreva um programa que pergunte a quantidade de km percorridos
por um carro alugado pelo usuário, assim como a quantidade de dias pelos quais
o carro foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60 por
dia e R$ 0,15 por km rodado '''

valor_dia_carro = 60.00
km_rodado = 0.15

aluguel_carro = int(input('Quantidade de dias alugados: '))
km = int(input('Digite a quantidade de km rodado: '))

valor_dias = aluguel_carro * valor_dia_carro
valor_km_rodado = km * km_rodado

print(f'Quantidade de dias de aluguel= {aluguel_carro}, no total de R${valor_dias:.2f}')
print(f'Quantidade de Km rodado= {km}km, no total de R${valor_km_rodado:.2f}')
print(f'Totalizando: R${valor_dias + valor_km_rodado:.2f}')

