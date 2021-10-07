import random

def jogar():

    msg_de_abertra()
    palavra_secreta = carrega_palavra_secreta()
    letras_acertadas = inicializa_letras_acertada(palavra_secreta)

    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)

    while(not enforcou and not acertou):

        chute = input('Qual a letra? ')
        chute = chute.strip().upper()

        if(chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if (chute == letra):
                    letras_acertadas[index] = letra
                index += 1
        else:
            erros += 1
        
        enforcou = erros == 6
        acertou = '_' not in letras_acertadas
        print(letras_acertadas)

    if(acertou):
        print('Você ganhou!!')
    else:
        print('Você perdeu!!')

print('Fim de jogo!')


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
    return palavra
    
if(__name__ == "__main__"): #garante a execução como programa principal:
    jogar()

