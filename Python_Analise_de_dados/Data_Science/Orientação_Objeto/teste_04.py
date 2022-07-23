""" Metodos Especiais """

# Criando uma class Livro
class Livro():
    # Criando o método construtor
    def __init__(self, titulo, autor, paginas) -> None:
        print('Livro criado')
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
    
    # Método para retornar um texto
    def __str__(self) -> str:
        return f'Titulo: {self.titulo}, Autor: {self.autor}, paginas: {self.paginas}'
    
    def __len__(self):
        return self.paginas
    
    def len(self):
        return f'Paginas do livro com método comum: {self.paginas}'
     
# Instanciando um objeto da class Livro()
livro = Livro('o senhor dos aneis', 'J.R.R. Tolkien', 576)
print(livro)
print(livro.len())
print(len(livro))