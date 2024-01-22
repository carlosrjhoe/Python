from datetime import datetime

class Pessoa:
    
    DATA = datetime.now()
    
    def __init__(self, nome, nascimento, comendo=False, falar=False):
        self.nome = nome
        self.nascimento = nascimento
        self.comendo = comendo
        self.falar = falar
        
    def get_idade(self):
        self.idade = int(self.DATA.year - self.nascimento)
        return self.idade
    
    def falando(self, assunto):
        if self.comendo:
            print(f'{self.nome.title()} Está comendo, não pode falar de boca cheia.')
            return
        
        print(f'{assunto}')
        self.comendo = False
        
    def informacao(self):
        print(f'{self.nome.title()} nasceu em {self.nascimento}, e tem {self.get_idade()} anos.')
    
    def comer(self, alimento):
        if self.comendo:
            print(f'{self.nome.title()} já está comendo.\n')
            return
        
        print(f'{self.nome.title()} está comendo {alimento}.')
        self.comendo = True
        
    def para_de_comer(self):
        if not self.comendo:
            print(f'{self.nome.title()} Não está comendo.')
            return
        
        print(f'{self.nome.title()} Parou de comer.')
        self.comendo = False