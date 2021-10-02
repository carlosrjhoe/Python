import forca
import adivinhacao

texto = 'ESCOLHA O JOGO'
print('#' * 45)
print(texto.center(45))
print('#' * 45)

print('(1) FOCA (2) ADIVINHAÇÃO')

jogo = int(input('Qualo jogo? '))

if(jogo == 1):
    print('Jogando forca.')
    forca.jogar()
elif(jogo == 2):
    print('Jogando adinihação')
    adivinhacao.jogar()