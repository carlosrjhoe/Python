def cabecalho():
    texto = 'JOGO DA ADIVINHAÇÃO'
    print(50*'*')
    print(f'{texto:*^50}')
    print(50*'*')

def advinhacao():
    tentativas = 3
    numero_secreto = 42
    
    for rodada in range(1, tentativas+1):
        print(f'{rodada}° rodada, você tem {tentativas} tentativas')
        chute = int(input('Digite o seu número: '))
        print(f'Você digitou: {chute}')
        
        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto
        
        if acertou: 
            print('Acertou!')
            break
        elif maior: 
            print('Você errou, o chute foi maior que o número secreto.')
            tentativas -= 1
        elif menor: 
            print('Você errou, o chute foi menor que o número secreto.')
            tentativas -= 1
    print('Fim de jogo!')
    
def main():
    cabecalho()
    advinhacao()
    
if __name__ == "__main__":
    main()