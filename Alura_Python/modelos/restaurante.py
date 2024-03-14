class Restaurante:

    restaurantes = []
    
    def __init__(self, nome, categoria, ativo=False):
        self._nome = nome.title()
        self.categoria = categoria.title()
        self._ativo = ativo
        Restaurante.restaurantes.append(self)

    @property
    def ativo(self):
        return '✔️' if self._ativo else '❎'

    def alterar_estado(self):
        self._ativo = not self._ativo

    def __str__(self) -> str:
        return f'{self._nome} - {self.categoria} - {self.ativo}'

    @classmethod
    def listar_restaurantes(cls) -> list:
        print(f'{"Nome do restaurante".ljust(25)} | {"Categoria".ljust(25)} | {"Status"}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante.categoria.ljust(25)} | {restaurante._ativo}')


            
if __name__ == "__main__":
    restaurante_1 = Restaurante('restaurante python', 'fastFood')
    restaurante_1.alterar_estado()
    restaurante_2 = Restaurante('restaurante java', 'pizza express')

    Restaurante.listar_restaurantes()