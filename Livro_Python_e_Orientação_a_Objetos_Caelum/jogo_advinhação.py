def cabecalho():
    texto = 'JOGO DA ADIVINHAÇÃO'
    print(50*'*')
    print(f'{texto:*^50}')
    print(50*'*')

def advinhacao():
    numero_secreto = 42

    chute = int(input('Digite o seu número: '))
    print(f'Você digitou: {chute}')
    if chute != numero_secreto:
        print('Você errou!')
    else:
        print('Acertou!')
    
def main():
    cabecalho()
    advinhacao()
    
if __name__ == "__main__":
    main()