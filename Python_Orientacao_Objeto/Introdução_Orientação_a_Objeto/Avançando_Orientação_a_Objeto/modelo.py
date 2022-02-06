class Filmes:
    def __init__(self, nome, ano, duracao):
        self.__nome = nome.title() # O title() é um método que retorna uma string onde o primeiro caractere em cada palavra é maiúsculo.
        self.ano = ano
        self.duracao = duracao
        self.__likes = 0
        
    @property
    def likes(self):
        return self.__likes
        
    def dar_like(self):
        self.__likes += 1
        
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome.title()
        
class Series:
    def __init__(self, nome, ano, temporada):
        self.__nome = nome.title()
        self.ano = ano
        self.temporada = temporada
        self.__likes = 0
    
    @property
    def likes(self):
        return self.__likes
        
    def dar_like(self):
        self.__likes += 1
        
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome.title()
    
        
vingadores = Filmes('vingadores', 2018, 150)
smallville = Series('smallville', 2012, 10)


print(f'Filme: {vingadores.nome} - Ano: {vingadores.ano} - Duração: {vingadores.duracao} Likes: {vingadores.likes}')
print(f'Série: {smallville.nome} - Ano: {smallville.ano} - Temporada: {smallville.temporada} Likes: {smallville.likes}')

