def jogar():
    texto = 'JOGO DA FORCA'
    print('#' * 45)
    print(texto.center(45))
    print('#' * 45)

    palavra_secreta = 'banada'
    enforcou = False
    acertou = False

    print(palavra_secreta)

    while(not enforcou and not acertou):
        chute = input('Qual a letra: ')
        chute = chute.strip()

        index = 0
        for letra in palavra_secreta:
            if (chute.upper() == letra.upper()):
                print(f'Encontrei a letra {letra} na posição {index}')
            index = index + 1
        print('Jogando...')
    print('Fim de jogo!')

if(__name__ == "__main__"): #garante a execução como programa principal:
    jogar()