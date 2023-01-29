tabuleiro = {
    "Top-Esquerdo": "", "Top-Meio": "", "Top-Direito": "",
    "Mid-Esquerdo": "", "Mid-Meio": "", "Mid-Direito": "",
    "Low-Esquerdo": "", "Low-Meio": "", "Low-Direito": "",
}


def mostrarTabuleiro(tabuleiro):
    print(f'{tabuleiro["Top-Esquerdo"]}|{tabuleiro["Top-Meio"]}|{tabuleiro["Top-Direito"]}')
    print('-+-+-')
    print(f'{tabuleiro["Mid-Esquerdo"]}|{tabuleiro["Mid-Meio"]}|{tabuleiro["Mid-Direito"]}')
    print('-+-+-')
    print(f'{tabuleiro["Low-Esquerdo"]}|{tabuleiro["Low-Meio"]}|{tabuleiro["Low-Direito"]}')
    print('-+-+-')


def jogoDaVelha(tabuleiro):
    turn = "X"
    for i in range(9):
        mostrarTabuleiro(tabuleiro)
        i = input(f'Vire para {turn}. Mover em qual espaço? ')
        tabuleiro[i] = turn
        if turn == "X":
            turn = "O"
        else:
            turn = "X"

    mostrarTabuleiro(tabuleiro)


if __name__ == '__main__':
    print(tabuleiro)
    jogoDaVelha(tabuleiro)