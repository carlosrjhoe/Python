"""
    varialvel -> public - legenda: Pode mecher
    _variavel -> protected - legenda: Não pode mecher
    __variavel -> private - legenda: INTOCÁVEL
    
"""

class BaseDeDados:
    def __init__(self):
        self.__dados = {}
        
    def inserir_cliente(self, id, nome):
        if 'clientes' not in self.__dados:
            self.__dados['clientes'] = {id: nome}
        else:
            self.__dados['clientes'].update({id: nome})
            
    def listar_dados(self):
        for id, nome in self.__dados['clientes'].items():
            print(f'{id} - {nome.title()}')
    
    def apagar_cliente(self, id):
        del self.__dados['clientes'][id]