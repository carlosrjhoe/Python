class Decoradores:
    
    def __init__(self) -> None:
        texto = 'Programa que irá estilizar strings'
        print(f'{"#"*len(texto)}')
        print(f'{texto.center(len(texto))}')
        print(f'{"#"*len(texto)}')
        
        self.palavra = ''
        
    def aplicar_estilo(self):
        self.palavra = input('Digite uma palavra: ')
        
    def negrito(self):
        print(f"<b>",self.aplicar_estilo(),"</b>")
        
    def italico(self):
        print(f"<i>"'{self.palavra}'"</i>")
        
    def sublinhado(self):
        print(f"<u>"'{self.palavra}'"</u>")
    
        
        