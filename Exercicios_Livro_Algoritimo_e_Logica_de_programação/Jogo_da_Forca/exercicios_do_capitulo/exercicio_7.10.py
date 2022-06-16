"""Exercício 7.10"""

# O tabuleiro
velha = """ Posições
   |   |      7 | 8 | 9
---+---+---  ---+---+---
   |   |      4 | 5 | 6
---+---+---  ---+---+---
   |   |      1 | 2 | 3
"""

posicoes = [
    None, # Elemento adicionado para facilitar índices
    (5, 1) #1
    (5, 5) #2
    (5, 9) #3
    (3, 1) #4
    (3, 5) #5
    (3, 9) #6
    (1, 1) #7
    (1, 5) #8
    (1, 9) #9
]

"""Posições que levam ao ganho do jogo
Jogadas fazendo uma linha, um coluna ou as diagonais ganham
Os números representam as posições ganhadoras"""

ganho = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [7,4,1],
    [8,5,2],
    [9,6,3],
    [7,5,3],
    [1,5,9]
]

"""Constroi o tabuleiro a partir das strings
gerando uma lista de listas que pode ser modificada"""

tabuleiro = []
for linha in velha.splitlines():
    tabuleiro.append(list(linha))