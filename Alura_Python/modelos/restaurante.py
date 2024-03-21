from modelos.avaliacao import Avaliacao
from modelos.cardapio.item_cardapio import ItemCardapio

class Restaurante:

    restaurantes = []
    
    def __init__(self, nome, categoria, ativo=False):
        self._nome = nome.title()
        self.categoria = categoria.title()
        self._ativo = ativo
        self._avaliacao = []
        Restaurante.restaurantes.append(self)
        self._cardapio = []

    @property
    def ativo(self):
        return f'✔️' if self._ativo else '❎'

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
        if 0 < nota <= 5:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)

    @property
    def media_avaliacao(self):
        if not self._avaliacao:
            return '-'
        else:
            soma_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
            quantidade_notas = len(self._avaliacao)
            media = round(soma_notas / quantidade_notas, 1)
            return media

    def adicionar_no_cardapio(self, item):
        if isinstance(item, ItemCardapio):
            self._cardapio.append(item)

    @property
    def exibir_cardapio(self):
        print(f'Cardapio do restaurante {self._nome}\n')
        for num, item in enumerate(self._cardapio, start=1):
            if hasattr(item, 'descricao'):
                msg = f'{num}. Nome: {item._nome} | Preço: R$ {item._preco:.2f} | Descrição: {item.descricao}'
                print(msg)
            else:
                msg_bebida = f'{num}. Nome: {item._nome} | Preço: R$ {item._preco:.2f} | Tamanho: {item.tamanho}'
                print(msg_bebida)