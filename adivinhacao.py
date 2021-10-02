import random

def jogar():

    texto = 'ADIVINHA'
    print('#' * 45)
    print(f'{texto:^45}')
    print('#' * 45)

    numero_secreto = random.randrange(100)
    total_tentativas = 0
    pontos = 1000

    print('Defina o nével de dificudade!')
    print('(1) Fácio (2)Médio (3)Difícil')
    nivel = int(input('Defina o nível: '))

    if(nivel == 1):
        total_tentativas = 15
    elif(nivel == 2):
        total_tentativas = 10
    else:
        total_tentativas = 5


    for rodada in range(1, total_tentativas + 1):
        print(f'Tentativa {rodada} de {total_tentativas}')
        chute_str = input("Digite um número entre 1 e 100: ")
        print("Você digitou: ", chute_str)
        chute = int(chute_str)

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto


        if (acertou):
            print(f"Você acertou e fez {pontos} pontos")
            break
        else:
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos
            if(maior):
                print('Você errou! O chupe foi maior que numero secreto...')
                if(rodada == total_tentativas):
                    print(f'O número secreto era {numero_secreto}. Você fez {pontos} pontos')
            elif(menor):
                print('Você errou! O chute foi menor que o numero secreto...')
                if(rodada == total_tentativas):
                    print(f'O número secreto era{numero_secreto}. Você fez {pontos}')
    print('Fim de jogo!')

if(__name__ == "__main__"): #garante a execução como programa principal:
    jogar()
