class Filmes:
    
    def __init__(self, nome, ano, duracao):
        self.nome = nome
        self.ano = ano
        self.duracao = duracao
        
class Series:
    
    def __init__(self, nome, ano, temporada):
        self.nome = nome
        self.ano = ano
        self.temporada = temporada
        
        
vingadores = Filmes('Vingadores', 2018, 150)
Smallville = Series('Smallville', 2012, 10)

print(f'Filme: {vingadores.nome} - Ano: {vingadores.ano} - Duração: {vingadores.duracao}')
print(f'Série: {Smallville.nome} - Ano: {Smallville.ano} - Temporada: {Smallville.temporada}')