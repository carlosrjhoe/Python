""" Jogo da forca com Programação Orientada a Objeto"""

import random 
tabuleriro = ['''
>>>>>>>>Forca<<<<<<<<<
+---+
|   |
|
|
|
|
=========''', '''
+---+
|   |
|   O
|
|
|
=========''','''
+---+
|   |
|   O
|   |
|
|
=========''','''
+---+
|   |
|   O
|   |\
|
|
=========''','''
+---+
|   |
|   O
|  /|\
|
|
=========''','''
+---+
|   |
|   O
|  /|\
|  /
|
=========''','''
+---+
|   |
|   O
|  /|\
|  / \
|
========='''
]

''' Início '''

class Enforcado():
    # Método construtor
    def __init__(self, palavra) -> None:
        self.palavra = palavra
        self.letra_errada = []
        self.letra_certa = []
    
    # Método para adivinhar uma letra
    def chute(self, letra):
        if letra in self.palavra and letra not in self.letra_certa:
            self.letra_certa.append(letra)
        elif letra not in self.palavra and  letra not in self.letra_errada:
            self.letra_errada.append(letra)
        else:
            return False
        return True
    
    # Método para verificar se o jogo terminou
    def jogo_perdido(self):
        return self.jogo_vencido() or (len(self.letra_errada) == 6)
    
    # Método para verificar se o jogo foi vencido
    def jogo_vencido(self):
        if '_' not in self.mostrar_letra():
            return True
        return False
        
    # Método para verificar mostrar a letra no tabuleiro
    def mostrar_letra(self):
        rtn = ''
        for letra in self.palavra:
            if letra not in self.letra_certa:
                rtn += '_'
            else:
                rtn += letra
        return rtn
        
        
    # Método para verificar status e imprimir no tabukeiro da forca
    def checar_status(self):
    
# Função para ler uma palavra de forma aleatória do banco de palavras
def escolher_palavra():
    with open('palavras.txt', 'rt') as f:
        bank = f.readlines()
    return bank[random.randint(0, len(bank))].strip()

# Função menu - Execução do programa
def menu():
    jogo = Enforcado(escolher_palavra())
    
    jogo.checar_status()
    
    if jogo.
    