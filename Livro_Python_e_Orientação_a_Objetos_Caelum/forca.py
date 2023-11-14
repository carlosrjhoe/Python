def cabecalho():
    texto = 'BEM VINDO AO JOGO DA FORCA'
    print(50*'*')
    print(f'{texto:*^50}')
    print(50*'*')

def main():
    cabecalho()
    
    palavra_secreta	= 'banana'
    letras_acertadas = ['_', '_', '_', '_', '_', '_']
    
    acertou = False
    enforcou = False
    erros = 0

    while(not enforcou and not acertou):
        chute = input('Digite uma letra: ')
        if (chute in palavra_secreta):
            posicao = 0
            for letra in palavra_secreta:
                if (chute.upper() == letra.upper()):
                    letras_acertadas[posicao] = letra
                posicao += 1
                acertou = True
            if acertou:
                print('Você acertou!')
        else:
            print('Você errou!')
            erros += 1

        enforcou = erros == 6
        acertou = '_' not in letras_acertadas
        print(letras_acertadas)

    print('Fim de jogo!')
    
if __name__ == "__main__":
    main()