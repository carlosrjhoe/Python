class Pessoa:
    def __init__(self, nome, profissao):
        self.nome = nome
        self.profissao = profissao

    def __repr__(self):
        return f'{self.nome} trabalha como {self.profissao}'

if __name__ == "__main__":
    pessoa1 = Pessoa('Carlos', 'Encarregado de manutenção')

print(pessoa1)