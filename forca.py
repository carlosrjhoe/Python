def jogar():
    texto = 'JOGO DA FORCA'
    print('#' * 45)
    print(texto.center(45))
    print('#' * 45)

    palavra_chave = 'banada'
    enforcou = False
    acertou = False

    while(not enforcou and not acertou):
        print('Jogando...')

if(__name__ == "__main__"): #garante a execução como programa principal:
    jogar()