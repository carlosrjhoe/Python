class Restaurante:
    
    def __init__(self, nome, categoria, ativo=False):
        self.nome = nome
        self.categoria = categoria
        self.ativo = ativo

    def __str__(self) -> str:
        return f'{self.nome} - {self.categoria} - {self.ativo}'

if __name__ == "__main__":
    restaurante = Restaurante('Restaurante Python', 'FastFood')
    print(restaurante)