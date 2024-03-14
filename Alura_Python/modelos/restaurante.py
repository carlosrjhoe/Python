from modelos.avaliacao import Avaliacao

class Restaurante:

    restaurantes = []
    
    def __init__(self, nome, categoria, ativo=False):
        self._nome = nome.title()
        self.categoria = categoria.title()
        self._ativo = ativo
        self._avaliacao = []
        Restaurante.restaurantes.append(self)

    @property
    def ativo(self):
        return '✔️' if self._ativo else '❎'

    def alterar_estado(self):
        self._ativo = not self._ativo

    def __str__(self) -> str:
        return f'{self._nome} - {self.categoria} - {self._ativo}'

    @classmethod
    def listar_restaurantes(cls) -> list:
        print(f'{"Nome do restaurante".ljust(25)} | {"Categoria".ljust(25)} | {"Avaliação".ljust(25)} | {"Status"}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante.categoria.ljust(25)} | {str(restaurante.media_avaliacao).ljust(25)} | {restaurante._ativo}')

    def receber_avaliacao(self, cliente, nota):
        avaliacao = Avaliacao(cliente, nota)
        self._avaliacao.append(avaliacao)

    @property
    def media_avaliacao(self):
        if not self._avaliacao:
            return 0
        else:
            soma_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
            quantidade_notas = len(self._avaliacao)
            media = round(soma_notas / quantidade_notas, 1)
            return media

# Nome do restaurante       | Categoria                 | Avaliação                 | Status
# Restaurante Python        | Fastfood                  | 8.3                       | True
# Restaurante Java          | Pizza Express             | 5.7                       | False
# Restaurante Javascript    | Comida Japonesa           | 6.3                       | True
# Restaurante Ruby          | Comida Tailandesa         | 4.7                       | False