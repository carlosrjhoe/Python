texto = 'JOGO DE ADIVINHAÇÃO'
print('*' * 45)
print(f'{texto:^45}')
print('*' * 45)

secreto = 42
tentativas = 3
rodada = 1

while tentativas > 0:
    print(f'Rodada {rodada}, restam {tentativas} tentativas.')
    chute = int(input('Digite o seu número: '))
    print(f'Você digitou {chute}.')

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
    tentativas -= 1
    rodada += 1
print('Fim de jogo')