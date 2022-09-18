class Gerador:
    
    def __init__(self) -> None:
        self.texto = 'Programa que vai gerar uma lista'
        print(f'{"#"*len(self.texto)}')
        print(f'{self.texto.center(len(self.texto))}')
        print(f'{"#"*len(self.texto)}')
        
        self.lista_1 = []
        self.lista_2 = []
        
    def gerar_lista(self):
        for i in range(51):
            self.lista_1.append(i)
            
        # Um for com listComprehension
        self.lista_2 = [j for j in range(51)]
            
    def exibir_lista(self):
        print(f'{self.lista_1}')
        print(f'{self.lista_2}')