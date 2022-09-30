"""
    Agregação. É um tipo especial de associação onde tenta-se demonstrar que as informações de um objeto (chamado objeto-todo) precisam ser complementados pelas informações contidas em um ou mais objetos de outra classe (chamados objetos-parte) conhecemos como todo/parte. Porém essas partes podem existir separadamente

"""

class CarrinhoDeCompras:
    def __init__(self):
        self.produtos = []

    def inserir_produto(self, produto):
        """Vai inserir um produto na lista de produtos vazia"""
        self.produtos.append(produto)

    def lista_produtos(self):
        """Vai listar os produto inseridos na lista produtos"""
        for produto in self.produtos:
            print(f'{produto.nome.title()} - R${produto.valor:.2f}')
            
    def soma_total(self):
        """Vai somar o valor total dos produtos inseridos na lista produtos"""
        total = 0
        for produto in self.produtos:
            total += produto.valor
        print(f'Total = R${total:.2f}')
        return
            
class Produto:
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor