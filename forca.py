def jogar():
    texto = 'JOGO DA FORCA'
    print('#' * 45)
    print(texto.center(45))
    print('#' * 45)

    palavra_secreta = 'banana'
    letras_acertadas = ['_','_','_','_','_','_']
    letras_faltando = str(letras_acertadas.count('_'))
    print(f'Ainda faltam acertar {letras_faltando} letras')

    enforcou = False
    acertou = False

    print(letras_acertadas)

    while(not enforcou and not acertou):
        chute = input('Qual a letra: ')
        chute = chute.strip()

        index = 0
        for letra in palavra_secreta:
            if (chute.upper() == letra.upper()):
                letras_acertadas[index] = letra
            index = index + 1
        print(letras_acertadas)
    print('Fim de jogo!')

if(__name__ == "__main__"): #garante a execução como programa principal:
    jogar()