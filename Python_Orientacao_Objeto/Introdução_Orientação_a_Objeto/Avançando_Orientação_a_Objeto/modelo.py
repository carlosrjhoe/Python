class Programa:
    
    def __init__(self, nome, ano):
        self._nome = nome.title() # O title() é um método que retorna uma string onde o primeiro caractere em cada palavra é maiúsculo.
        self.ano = ano
        self._likes = 0
        
    @property
    def likes(self):
        return self._likes
        
    def dar_like(self):
        self._likes += 1
        
    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, nome):
        self._nome = nome

class Filmes(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao
        
class Series(Programa):
    def __init__(self, nome, ano, temporada):
        super().__init__(nome, ano)
        self.temporada = temporada


vingadores = Filmes('vingadores', 2018, 150)
smallville = Series('smallville', 2012, 10)
vingadores.dar_like()
vingadores.dar_like()
smallville.dar_like()
vingadores.dar_like()
smallville.dar_like()

print(f'Filme: {vingadores.nome} - Ano: {vingadores.ano} - Duração: {vingadores.duracao} - Likes: {vingadores.likes}')
print(f'Série: {smallville.nome} - Ano: {smallville.ano} - Temporada: {smallville.temporada} - Likes: {smallville.likes}')

