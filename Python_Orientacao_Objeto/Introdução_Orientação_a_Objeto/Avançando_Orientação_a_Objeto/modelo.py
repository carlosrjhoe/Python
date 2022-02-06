from os import link


class Programa:
    def __init__(self, nome, ano, likes):
        self._nome = nome.title() # O title() é um método que retorna uma string onde o primeiro caractere em cada palavra é maiúsculo.
        self._ano = ano
        self._likes = likes
        
    @property
    def likes(self):
        return self._likes
        
    def dar_like(self):
        self._likes += 1
        
    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()
        
        
class Filmes(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao
        
class Series(Programa):
    def __init_(self, nome, ano, temporada):
        super().__init__(nome, ano)
        self.temporada = temporada
    
    
vingadores = Filmes('vingadores', 2018, 150)
smallville = Series('smallville', 2012, 10)

print(f'Filme: {vingadores.nome} - Ano: {vingadores.ano} - Duração: {vingadores.duracao} Likes: {vingadores.likes}')
print(f'Série: {smallville.nome} - Ano: {smallville.ano} - Temporada: {smallville.temporada} Likes: {smallville.likes}')

