# Criando uma Classe
# class Livro():
#   def __init__(self, titulo, isbn):
#     self.titulo = titulo
#     self.isbn = isbn
#     print('Construtor chamado para criar um objeto desta classe.')
    
#   def imprime(self):
#     print(f'Foi criado o livro {self.titulo} e ISBN é {self.isbn}')
    
# Livro_01 = Livro('A menina que roubava livros', 7161514)

# print(type(Livro_01))
# Livro_01.imprime()

class Cachorro():
  def __init__(self, raca) -> None:
    self.raca = raca
    
rex = Cachorro(raca='labrador')
print(rex.raca)

tufik =Cachorro(raca="poddle")
print(tufik.raca)