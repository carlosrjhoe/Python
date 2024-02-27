class BaseDeDados:
    def __init__(self):
        self.__base = {}

    def inserir(self, nome, fone):
        if 'clientes' not in self.__base:
            self.__base['clientes'] = {nome:fone}
        else:
            self.__base['clientes'].update({nome:fone})

    def listar(self):
        for nome, fone in self.__base['clientes'].items():
            print(f'Nome: {nome.title()} - Fone: {fone}')

    def apagar(self, nome):
        del self.__base['clientes'][nome]