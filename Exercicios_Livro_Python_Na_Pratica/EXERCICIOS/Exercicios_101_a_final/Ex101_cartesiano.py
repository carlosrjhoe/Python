import math


class cartesiano:
    
    def __init__(self) -> None:
        texto = 'Programa que mostra a coordenada do plano cartesiano'
        print(f'{"#"*len(texto)}')
        print(f'{texto.center(len(texto))}')
        print(f'{"#"*len(texto)}')
        
        self.posicao = [0,0]
        self.coordenada = ''
        self.movimento = ''
        self.direcao = ''
        self.passos = ''
        
    def pergunta_coordenada(self):
        while True:
            self.coordenada = input('Digite a coordenada, seguido do número de passos: ').upper()
            if not self.coordenada:
                break
            self.movimento = self.coordenada.split(' ')
            self.direcao = self.movimento[0]
            self.passos = int(self.movimento[1])
            
            if self.direcao == 'CIMA':
                self.posicao[0] += self.passos
            elif self.direcao == 'BAIXO':
                self.posicao[0] -= self.passos
            elif self.direcao == 'ESQUERDA':
                self.posicao[1] -= self.passos
            elif self.direcao == 'DIREITA':
                self.posicao[1] += self.passos
            else:
                pass
            
    def exibir_coordenadas(self):
        print(int(round(math.sqrt(self.posicao[1]**2+self.posicao[0]**2))))
        print(self.posicao)