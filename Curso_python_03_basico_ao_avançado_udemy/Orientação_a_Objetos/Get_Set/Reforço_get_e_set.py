# SETTER = CONFIGURAR UM VALOR (=)
# GETTER = OBTER (RETORNAR) O VALOR QUE FOI CONFIGURADO NO SETTER

class Pessoa:
    def __init__(self, nome):
        self.nome = nome
    
    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        print('Foi executado!')
        self._nome = nome
    