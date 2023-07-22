class Pessoa:
    def __init__(self, nome, sobreNome):
        self.nome = nome
        self.sobreNome = sobreNome

pessoa = Pessoa(nome='carlos', sobreNome='junior')
setattr(pessoa, pessoa.nome, pessoa.sobreNome)
inf_1 = getattr(pessoa, pessoa.nome)

print(inf_1)
