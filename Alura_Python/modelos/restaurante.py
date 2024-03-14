class Restaurante:

    restaurantes = []
    
    def __init__(self, nome, categoria, ativo=False):
        self.nome = nome
        self.categoria = categoria
        self.ativo = ativo
        Restaurante.restaurantes.append(self)

    def __str__(self) -> str:
        return f'{self.nome} - {self.categoria} - {self.ativo}'

    def listar_restaurantes() -> list:
        for restaurante in Restaurante.restaurantes:
            print(f'{restaurante.nome} | {restaurante.categoria} | {restaurante.ativo}')

            
if __name__ == "__main__":
    restaurante_1 = Restaurante('Restaurante Python', 'FastFood')
    restaurante_2 = Restaurante('Restaurante Java', 'Pizza Express')

    Restaurante.listar_restaurantes()