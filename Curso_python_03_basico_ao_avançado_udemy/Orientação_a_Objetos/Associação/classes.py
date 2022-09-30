class Escritor:
    def __init__(self, nome):
        self.__nome = nome
        self.__ferramenta = None
        
    @property
    def get_nome(self):
        return self.__nome.title()
    
    @property
    def get_ferramenta(self):
        return self.__ferramenta
    
    @get_ferramenta.setter
    def get_ferramenta(self, ferramenta):
        self._ferramenta = ferramenta
    

class Caneta:
    def __init__(self, marca):
        self.__marca = marca
        
    @property
    def get_marca(self):
        return self.__marca
    
    def escrever(self):
        print('Caneta está escrevendo..')
        
        
class MaquinaDeEscrever:
    def escrever(self):
        print('Maquina está escrevendo')