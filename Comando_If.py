secreto = 5
chute = int(input('Digite um numero de [0 a 10]: '))
acertou = chute == secreto
maior = chute > secreto
menor = chute < secreto

if acertou:
    print('Você acertou')
elif maior:
    print('Você errou! O chute foi maior que o número secreto')
elif menor:
    print('Voce errou! O chute foi menor que o número secreto')
