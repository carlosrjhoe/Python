from operator import attrgetter

class Pessoa(object):
    def __init__(self, nome, renda, telefone):
        self.nome = nome
        self.renda = renda
        self.telefone = telefone

    def __repr__(self) -> str:
        return f'Nome:{self.nome} - R${self.renda:.2f} - Tel.:{self.telefone}'

clientes = [
    Pessoa('Carlos', 3321, 987654321),
    Pessoa('Mayara', 2321, 987651234),
    Pessoa('Neto', 31, 987654567),
    Pessoa('Luna', 21, 987651423),
]

clientes.sort(key=attrgetter('nome'))
print(clientes)