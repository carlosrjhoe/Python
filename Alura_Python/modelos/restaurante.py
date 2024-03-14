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

    def __str__(self) -> str:
        return f'{self._nome} - {self.categoria} - {self.ativo}'

    def listar_restaurantes() -> list:
        print(f'{"Nome do restaurante".ljust(25)} | {"Categoria".ljust(25)} | {"Status"}')
        for restaurante in Restaurante.restaurantes:
            print(f'{restaurante.nome.ljust(25)} | {restaurante.categoria.ljust(25)} | {restaurante.ativo}')

            
if __name__ == "__main__":
    restaurante_1 = Restaurante('restaurante python', 'fastFood')
    restaurante_2 = Restaurante('restaurante java', 'pizza express')

    Restaurante.listar_restaurantes()