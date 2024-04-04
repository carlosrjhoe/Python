"""Exercício 4.2 Escreva um programa que pergunte a velocidade do carro de um
usuário. Caso ultrapasse 80 km/h, exiba uma mensagem dizendo que o usuário
foi multado. Nesse caso, exiba o valor da multa, cobrando R$ 5 por km acima de
80 km/h"""

velocidade = int(input('Digite a velocidade do veiculo [Km/h]: '))
VELOCIDADE_MAXIMA = 80
MULTA = 5.00
multa_por_velocidade = (velocidade - VELOCIDADE_MAXIMA) * MULTA

if velocidade > VELOCIDADE_MAXIMA:
    print(f'Você ultrapassou velocidade maxima.')
    print(f'Sua velocidade é de {velocidade}Km/h')
    print(f'Você esta sendo multado em R$ {multa_por_velocidade:.2f}')
else:
    print('Siga em frente, cuidado na pista...')