class Programa:
    
    def __init__(self, nome, ano):
        self._nome = nome.title()
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
        
    def __str__(self):
        return (f'{self._nome} - {self.ano} - {self._likes} likes')

class Filmes(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao
        
    def __str__(self):
        return (f'{self._nome} - {self.ano} - {self.duracao} min - {self._likes} likes')
        
class Series(Programa):
    def __init__(self, nome, ano, temporada):
        super().__init__(nome, ano)
        self.temporada = temporada
        
    def __str__(self):
        return (f'{self._nome} - {self.ano} - {self.temporada} temporadas - {self._likes} likes')

class Playlist:
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas
        
    @property
    def listagem(self):
        return self._programas
    
    
    def __len__(self):
        return len(self._programas)
        

vingadores = Filmes('vingadores', 2018, 150)
smallville = Series('smallville', 2012, 10)
tmep = Filmes('todo mundo em panico', 1999, 100)
demolidor = Series('demolidor', 2016, 2)

vingadores.dar_like()
tmep.dar_like()
tmep.dar_like()
vingadores.dar_like()
demolidor.dar_like()
demolidor.dar_like()
vingadores.dar_like()
smallville.dar_like()
demolidor.dar_like()
smallville.dar_like()
tmep.dar_like()

filmes_e_series = [vingadores, smallville, demolidor, tmep]
playlist_fim_de_semana = Playlist('fim de semana', filmes_e_series)

print(f'Tamanho da playlist: {len(playlist_fim_de_semana)}')
for programa in playlist_fim_de_semana.listagem:
    print(programa)
    
    
'''
SOBRE __INIT__:
    É um método, que por definição, é executada sempre que instanciamos um objeto.
    
SOBRE SELF:
    O self é um parâmetro obrigatório que receberá a instância criada. Ao contrário de muitas linguagens, ele deve ser explícito. E também ao contrário de muitas linguagem que criam o objeto durante o construtor, Python cria o objeto e passa ele para o construtor complementar com as primeiras ações necessárias quando ele é construído.

SOBRE @PROPERTY:
    Você pode definir propriedades com a sintaxe @property, que é mais compacta e legível.
    O uso de @property pode ser considerada a maneira "pytônica" de definir getters, setters e deleters.
    Ao definir propriedades, você pode alterar a implementação interna de uma classe sem afetar o programa, para adicionar getters setters e deleters que atuam como intermediários "nos bastidores" para evitar acessar ou modificar osdadosdiretamente.
    
SOBRE SETTER:
    Esses são os métodos usados ​​no recurso OOPS que ajudam a definir o valor para atributos privados em uma classe .

SOBRE __str__:
    É um método especial, como __init__, usado para retornar uma representação de string de um objeto.
    Quando escrevo uma nova classe, quase sempre começo escrevendo __init__, o que facilita a instanciação de objetos, e __str__, que é útil para a depuração.
'''