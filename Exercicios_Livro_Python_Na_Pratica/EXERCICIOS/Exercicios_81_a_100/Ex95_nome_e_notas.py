from operator import itemgetter

class Escola():
    
    def __init__(self):
        # Construtor/inicializador
        self.nomes = [] # Atributo com lista vazia.
    
    def recebe_dados(self):
        while True:
            self.dados = input('Digite seu nome, seguido de duas notas de [0 a 10]: ')
            if not self.dados:
                break
            self.nomes.append(tuple(self.dados.split(',')))
        
    def exibe_dados(self):
        return print(f'{sorted(self.nomes, key= itemgetter(0,1,2))}')
    
aluno = Escola()
aluno.recebe_dados()
aluno.exibe_dados()