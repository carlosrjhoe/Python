class Combinacoes:
    
    def __init__(self) -> None:
        self.texto = 'Programa que vai gerar possiveis combinações entre numeros'
        print(f'{"#"*len(self.texto)}')
        print(f'{self.texto.center(len(self.texto))}')
        print(f'{"#"*len(self.texto)}')
        
        self.lista_1 = []
        self.lista_2 = []
        
    def gerar_lista(self):
        for i in [1,2,3]:
            for j in [4,5,6]:
                if i != j:
                    self.lista_1.append((i,j))
            
        # Um for com listComprehension
        self.lista_2 = [(i,j) for i in[1,2,3] for j in [4,5,6] if i != j]
            
    def exibir_lista(self):
        print(f'{self.lista_1}')
        print(f'{self.lista_2}')