
class Estudante():
  # Classe
  def __init__(self, nome, idade, nota) -> None:
    # Construtor da Classe Estudante
    self.nome = nome
    self.idade = idade
    self.nota = nota
    
  def lista_Funcionarios(self):
    # Metodo de mostrar funcionário
    print(f'O aluno {self.nome}, tem {self.idade} anos de idade e tirou a nota {self.nota}')
    
carlos = Estudante('Carlos', 37, 8.9) # Estanciando um objeto da classe Estudante
mayara = Estudante('Mayara', 37, 10.0) # Estanciando um objeto da classe Estudante

carlos.lista_Funcionarios()
mayara.lista_Funcionarios()