from dataclasses import dataclass

# class Banco:
#     def __init__(self, agencias=list[int] | None, clientes=list[int] | None, contas=list[int] | None) -> None:
#         self.agencias = agencias
#         self.clientes = clientes
#         self.contas = contas

@dataclass
class Pessoa:
    nome: str
    sobrenome: str
    idade: int

    @property
    def nome_completo(self):
        return f'{self.nome} {self.sobrenome}'

    @nome_completo.setter
    def nome_completo(self, valor):
        nome, sobrenome = valor.split()
        self.nome = nome
        self.sobrenome = ' '.join(sobrenome)

if __name__ == '__main__':
    pessoa = Pessoa('Carlos', 'Conceição', 38)
    print(pessoa)