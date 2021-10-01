texto = 'JOGO DE ADIVINHAÇÃO'
print('*' * 45)
print('{:^45}'.format(texto))
print('*' * 45)

secreto = 42
tentativas = 3

for rodada in range(1, tentativas + 1):
    chute = int(input('Digite o seu número: '))
    

    acertou = chute == secreto
    maior = chute > secreto
    menor = chute < secreto

    if acertou:
        print('Você acertou!')
        break
    elif menor:
        print('Você ERROU! O seu chute é menor que o número secreto.')
    elif maior:
        print('Você ERROU! O seu chute é maior que o número secreto.')
print('Fim de jogo!')
