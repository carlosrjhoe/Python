class Pessoa:
    def __init__(self, nome, profissao):
        self.nome = nome
        self.profissao = profissao

    def __repr__(self):
        return f'{self.nome} trabalha como {self.profissao}'

if __name__ == "__main__":
    pessoa1 = Pessoa('Carlos', 'Encarregado de manutenção')

print(pessoa1)

primeiro_atributo = 'nome'
segundo_atributo = 'Fernando'

setattr(pessoa1, primeiro_atributo, segundo_atributo)
primeiro = getattr(pessoa1, primeiro_atributo)

print(primeiro)