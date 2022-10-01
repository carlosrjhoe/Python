""" 
    Composição. 
    É um dos conceitos fundamentais da Programação Orientada a Objetos. Neste conceito, descreveremos uma classe que faz referência a um ou mais objetos de outras classes  como uma variável de instância. 
"""

class Cliente:
    def __init__(self, nome, idade):
        self.nome = nome.title()
        self.idade = idade
        self.enderecos = []
        
    def inserir_endereco(self, cidade, estado):
        """Vai adicionar um endereço dentro de uma lista de endereços."""
        self.enderecos.append(Endereco(cidade, estado))
        
    def listar_enderecos(self):
        """Vai imprimir a lista de endereço dentro de endereços."""
        for endereco in self.enderecos:
            print(f'{endereco.cidade.title()} - {endereco.estado.upper()}')
            

class Endereco:
    def __init__(self, cidade, estado):
      self.cidade = cidade
      self.estado = estado