class Jogos:
    
    def __init__(self) -> None:
        self.texto = 'Jogo para mostrar qual é o maior numero'
        print(f'{"#"*len(self.texto)}')
        print(f'{self.texto.center(len(self.texto))}')
        print(f'{"#"*len(self.texto)}')
        
        self.numero_1 = ''
        self.numero_2 = ''
        self.numero_3 = ''
        self.maior = ''
        
    def perguntas(self):
        self.numero_1 = int(input('Digite um número: '))
        self.numero_2 = int(input('Digite outro número: '))
        self.numero_3 = int(input('Digite mais um número: '))
    
    def maior_de_tres(self):
        if self.numero_1 > self.numero_2 and self.numero_1 > self.numero_3:
            self.maior = self.numero_1
        elif self.numero_2 > self.numero_1 and self.numero_2 > self.numero_3:
            self.maior = self.numero_2
        else:
            self.maior = self.numero_3
        return print(f'O número {self.maior} é maior!')
            