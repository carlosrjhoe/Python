"""Exercício 4.1 Analise o programa da listagem 4.2. Responda o que acontece se o
primeiro e o segundo valores forem iguais? Explique"""

# Acontece que ele execulta as duas condiçoes...

idade_carro = int(input('Digite a idade do seu carro: '))

if idade_carro <= 3:
  print('Seu carro é novo.')
if idade_carro >= 3:
  print('Seu carro é velho...')