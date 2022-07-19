""" Jogo de advinhação """

import random

cont = 0

numeroSecreto = random.randint(1, 20)
print('Estou pensando em um número entre [1 e 20] Adivinhe.: ')

for chute in range(1, 7):
  # Peça para o jogador adivinhar 6 vezes
  print('Adivinhe...')
  chute = int(input())
  
  if chute < numeroSecreto:
    print('Seu chute foi muito baixo.')
    cont += 1
  elif chute > numeroSecreto:
    print('Seu chute foi muito alto.')
    cont += 1
  else:
    # Esta condição corresponde ao palpite correto!
    break
  
if chute == numeroSecreto:
  print(f'Bom trabalho! Você adivinhou meu número em {str(cont+1)} palpites.')
else:
  print(f'Não. O número que eu estava pensando era {str(numeroSecreto)}')