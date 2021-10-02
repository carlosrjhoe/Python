import random

texto = 'ADIVINHA'
print('#' * 45)
print(f'{texto:^45}')
print('#' * 45)

numero_secreto = random.randrange(10)
total_tentativas = 10



for rodada in range(1, total_tentativas + 1):
    print(f'Tentativa {rodada} de {total_tentativas}')
    chute_str = input("Digite um número entre 1 e 10: ")
    print("Você digitou: ", chute_str)
    chute = int(chute_str)

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto


    if (chute < 1 or chute > 100):
        print("Você deve digitar um número entre 1 e 100!")
        continue
    elif(acertou):
        print('Acretou!')
        break
    elif(maior):
        print('O chupe foi maior que numero secreto...')
    else:
        print('O chute foi menor que o numero secreto...')


    
