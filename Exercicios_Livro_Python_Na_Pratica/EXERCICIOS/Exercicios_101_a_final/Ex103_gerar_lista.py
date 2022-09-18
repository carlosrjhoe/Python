class Gerador:
    
    def __init__(self) -> None:
        self.texto = 'Programa que vai gerar uma lista'
        print(f'{"#"*len(self.texto)}')
        print(f'{self.texto.center(len(self.texto))}')
        print(f'{"#"*len(self.texto)}')
        
        self.lista = []
        
    def gerar_lista(self):
        for i in range(51):
            self.lista.append(i)
            
    def exibir_lista(self):
        print(f'{self.lista}')