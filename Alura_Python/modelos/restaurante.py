class Restaurante:
    
    def __init__(self, nome, categoria, ativo=False):
        self.nome = nome
        self.categoria = categoria
        self.ativo = ativo


if __name__ == "__main__":
    restaurante = Restaurante('Restaurante Python', 'FastFood')

    print(restaurante.nome)
    print(restaurante.categoria)
    print(vars(restaurante))