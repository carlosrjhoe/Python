class Conversor():
    
    def __init__(self):
        # Construtor/inicializador
        self.dados = '' # Atributo
    
    def recebe_dados(self):
        self.dados = input('Digite uma palavra/frase: ')
        
    def exibe_dados(self):
        return print(f'{self.dados.upper()}')
    
frase = Conversor()
frase.recebe_dados()
frase.exibe_dados()