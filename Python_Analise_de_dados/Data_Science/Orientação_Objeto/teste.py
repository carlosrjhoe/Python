# Criando uma Classe
class Livro():
  def __init__(self):
    self.titulo = 'O monge e o executivo'
    self.isbn = 99988877
    
  def imprime(self):
    print(f'Foi criado o livro {self.titulo} e ISBN é {self.isbn}')
    
Livro_01 = Livro()

print(type(Livro_01))
Livro_01.imprime()
