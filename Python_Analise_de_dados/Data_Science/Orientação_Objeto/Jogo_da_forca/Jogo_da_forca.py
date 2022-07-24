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
    
    # Método construtor + especificação do métodos
    def __init__(self, palavra) -> None:
        self.palavra = palavra
        self.letras_erradas = []
        self.letras_certas = []
    
    # Método para adivinhar uma letra
    def chute(self, letra):
        if letra in self.palavra and letra not in self.letras_certas:
            self.letras_certas.append(letra)
        elif letra not in self.palavra and  letra not in self.letras_erradas:
            self.letras_erradas.append(letra)
        else:
            return False
        return True
    
    # Método para verificar se o jogo terminou
    def jogo_perdido(self):
        return self.jogo_vencido() or (len(self.letras_erradas) == 6)
    
    # Método para verificar se o jogo foi vencido
    def jogo_vencido(self):
        if '_' not in self.mostrar_letra():
            return True
        return False
        
    # Método para verificar mostrar a letra no tabuleiro
    def mostrar_letra(self):
        rtn = ''
        for letra in self.palavra:
            if letra not in self.letras_certas:
                rtn += '_'
            else:
                rtn += letra
        return rtn
        
        
    # Método para checar o status do jogo e imprimir no tabuleiro da forca
    def checar_status(self):
        print(tabuleriro[len(self.letras_erradas)])
        print(f'\nPalavra: {self.mostrar_letra()}')
        print(f'\nLetras erradas: ',)
        for letra in self.letras_erradas:
            print(letra,)
        print()
        print('Letras corretas: ',)
        for letra in self.letras_certas:
            print(letra,)
        print()
    
# Método para ler uma palavra de forma aleatória do banco de palavras de um arquivo txt
def escolher_palavra():
    with open('palavras.txt', 'rt') as f:
        bank = f.readlines()
    return bank[random.randint(0, len(bank))].strip()

# Função menu - Execução do programa
def menu():
    
    # Objeto
    jogo = Enforcado(escolher_palavra())
    
    # Enquanto o jogo não tiver terminado, print do status, solicitar uma letra e faz a leitura do caractere.
    while not Enforcado.jogo_perdido():
        Enforcado.hecar_status()
        usuario = input('\nDigite uma letra: ')
        Enforcado.chute(usuario)
    
    # Verificar o status do jogo
    Enforcado.checar_status()
    
    # De acordo com o status, imprime a mensagem na tela para o usuário
    if Enforcado.jogo_vencido():
        print('\nParabens! Você venceu!!!')
    else:
        print('\nGame Over! Você perdeu!!!')
        print(f'A palavra era: {Enforcado.palavra}')
    print('\nFoi bom jogar com você! Agora vá estudar!\n')
    
# Executar o programa

    