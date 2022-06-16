"""Listagem 7.45 – Jogo da forca"""

palavra = input('Digite a pala secreta: ').lower().strip()
for x in range(100):
    print()
digitadas = []
acertos = []
erros = 0
while True:
    senha = ''
    for letra  in palavra:
        senha += letra if letra in acertos else '.'
    print(senha)
    if senha == palavra:
        print('Você acertou')
        break
    tentativas = input('\nDigite uma letra: ').lower().strip()
    if tentativas in digitadas:
        print('Você já tentou esta letra!')
        continue
    else:
        digitadas += tentativas
        if tentativas in palavra:
            acertos += tentativas
        else:
            erros += 1
            print('Você errou!')
    print('X==:==\nX  :  ')
    print('X  O  ' if erros >= 1 else 'X')
    linha2 = ''
    
    if erros == 2:
        linha2 = '  |  '
    elif erros == 3:
        linha2 = ' \| '
    elif erros >= 4:
        linha2 = ' \|/ '
        
    print(f'{linha2}')
    linha3 = ''
    
    if erros == 5:
        linha3 += ' / '
    elif erros >= 6:
        linha3 += ' / \ '
    print(f'{linha3}')
    print('X\n==========')
    if erros == 6:
        print('Enforcado!')
        break
            