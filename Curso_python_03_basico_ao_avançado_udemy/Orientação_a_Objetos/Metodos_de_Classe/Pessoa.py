class Pessoa:
    ano_atual = 2022
    
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        
    def get_ano_nascimento(self):
        print(f'{self.ano_atual - self.idade}')
        
    @classmethod
    def por_ano_nascimento(cls, nome, idade, ano_nascimento):
        idade = cls.ano_atual - ano_nascimento
        return cls(nome, idade)
        
        

carlos = Pessoa('carlos', 37)
mayara = Pessoa.por_ano_nascimento('mayara', 37, 1985)
print(carlos.idade)
carlos.get_ano_nascimento()