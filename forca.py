import random

def jogar():

    msg_de_abertra()
    palavra_secreta = carrega_palavra_secreta()

    letras_acertadas = inicializa_letras_acertada(palavra_secreta)
    print(letras_acertadas)

    enforcou = False
    acertou = False
    erros = 0

    while(not enforcou and not acertou):

        chute = pede_chute()

        if(chute in palavra_secreta):
           marca_chute_correto(chute, letras_acertadas, palavra_secreta)
        else:
            erros += 1
            desenha_forca(erros)
        
        enforcou = erros == 7
        acertou = '_' not in letras_acertadas

        print(letras_acertadas)

    if(acertou):
        imprime_vencedor()
    else:
        imprime_perdedor()

print('Fim de jogo!')

def imprime_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def imprime_perdedor(palavra_secreta):
    print('Você perdeu!!')
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("     ______________         ")
    print("    /              \       ")
    print("   /                \      ")
    print("/\/                  \/\  ")
    print("\ |   XXXX     XXXX  | /   ")
    print(" \|   XXXX     XXXX  |/     ")
    print("  |   XXX       XXX  |      ")
    print("  |                  |      ")
    print("  \__      XXX     __/     ")
    print("    |\     XXX     /|       ")
    print("    | |           | |        ")
    print("    | I I I I I I I |        ")
    print("    |  I I I I I I  |        ")
    print("    \_             _/       ")
    print("      \_         _/         ")
    print("        \_______/           ")

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")
        print()

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")
        print()

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")
        print()

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")
        print()

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")
        print()

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")
        print()

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")
        print(" |            ")
        print("_|___         ")
        print()
def marca_chute_correto(chute, letras_acertadas, palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if (chute == letra):
            letras_acertadas[index] = letra
        index += 1

def pede_chute():
    chute = input('Qual a letra? ')
    chute = chute.strip().upper()
    return chute

def inicializa_letras_acertada(palavra):
    return ['_' for letra in palavra]

def msg_de_abertra():
    texto = 'JOGO DA FORCA'
    print('#' * 45)
    print(texto.center(45))
    print('#' * 45)

def carrega_palavra_secreta():
    arquivo = open('palavra.txt', 'r')
    
    # Depois temos que criar uma lista e percorrer o arquivo. Cada linha do arquivo deve ser guardada nessa lista:

    palavra = []

    for linha in arquivo:
        linha = linha.strip() # Precisamos remover o \n ao final da linha, fazendo um .strip
        palavra.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavra))
    palavra_secreta = palavra[numero].upper()
    return palavra_secreta

if(__name__ == "__main__"): #garante a execução como programa principal:
    jogar()

