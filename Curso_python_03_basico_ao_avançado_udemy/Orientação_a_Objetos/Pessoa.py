class Pessoa:
    def __init__(self, nome, idade, comendo=False, falando=False):
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
    
    
    def comer(self, alimento):
        if self.comendo:
            print(f'{self.nome.title()} já está comendo.\n')
            return
        
        print(f'{self.nome.title()} está comendo {alimento}')
        self.comendo = True
        
        
   