"""16 – Crie uma classe Autor com atributos nome e ano_nascimento. Crie uma classe Livro com atributos titulo, ano_de_publicacao e autor. A classe Livro deve ter uma associação com a classe Autor. Instancie objetos das classes Autor e Livro, e teste a relação entre eles:"""

class Autor:
    def __init__(self, nome, ano_nascimento):
        self.nome = nome
        self.ano_nascimento = ano_nascimento

class Livro:
    def __init__(self, titulo, ano_de_publicacao, autor):
        self.titulo = titulo
        self.ano_de_publicacao = ano_de_publicacao
        self.autor = autor

if __name__ == '__main__':
    autor_01 = Autor('carlos', 1985)
    livro_01 = Livro('Python levado a sério', 2010, autor_01)

    print(f'{livro_01.titulo}')
    print(f'{livro_01.ano_de_publicacao}')
    print(f'{livro_01.autor.nome}')
    print(f'{livro_01.autor.ano_nascimento}')