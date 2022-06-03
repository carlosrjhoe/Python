''' Exercício 4.2 Escreva um programa que pergunte a velocidade do carro de um
usuário. Caso ultrapasse 80 km/h, exiba uma mensagem dizendo que o usuário
foi multado. Nesse caso, exiba o valor da multa, cobrando R$ 5 por km acima de
80 km/h '''

velocidade = int(input('Qual a velocidade do veiculo em [km]: '))
limite = 80
infracao = (velocidade - limite) * 5

if velocidade > limite:
  print(f'Você foi multado em R${infracao:.2f}')