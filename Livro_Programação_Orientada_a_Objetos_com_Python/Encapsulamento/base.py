class BaseDeDados:
    """Definir a visibilidade de uma variável por meio da forma com que declara, uma underline torna a mesma protegida, underline duplo a torna privada e imutável."""
    def __init__(self):
        self.__base = {}
        # self.__base = {} # Variável protegida
        # self.___base = {} # Variável privada

    def inserir(self, name, cell_phone):
        if 'clientes' not in self.__base:
            self.__base['clientes'] = {name:cell_phone}
        else:
            self.__base['clientes'].update({name:cell_phone})

    def listar(self):
        for n, c in self.__base['clientes'].items():
            print(f'Nome: {n.title()} - Celular: {c}')

    def apagar(self, name):
        del self.base['clientes'][name]

if __name__ == '__main__':
    relacionar_clientes = BaseDeDados()
    relacionar_clientes.inserir('carlos', 81999998888)
    relacionar_clientes.inserir('mayara', 81988887777)
    relacionar_clientes.inserir('neto', 81977776666)
    relacionar_clientes.inserir('luna', 81966665555)
    relacionar_clientes.listar()