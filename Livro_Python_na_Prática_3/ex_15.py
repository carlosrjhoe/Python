"""15 – Crie uma classe Pessoa com atributos nome e idade. Crie duas subclasses, Estudante e Professor, que herdam de Pessoa e adicionam atributos específicos (por exemplo, curso para Estudante e disciplina para Professor). Instancie objetos das subclasses e teste seus atributos e métodos."""

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

class Estudante(Pessoa):
    def __init__(self, nome, idade, curso):
        super().__init__(nome, idade)
        self.curso = curso

class Professor(Pessoa):
    def __init__(self, nome, idade, disciplina):
        super().__init__(nome, idade)
        self.disciplina = disciplina


if __name__ == '__main__':
    estudante_01 = Estudante('carlos', 37, 'ADS')
    professo_01 = Professor('rosiclé', 58, 'Geografia')

    print(f'{estudante_01.nome}')
    print(f'{estudante_01.idade}')
    print(f'{estudante_01.curso}')

    print(f'{professo_01.nome}')
    print(f'{professo_01.idade}')
    print(f'{professo_01.disciplina}')