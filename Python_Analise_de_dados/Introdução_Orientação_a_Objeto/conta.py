class Conta:    # CLASS

    def __init__(self, numero, titular, saldo, limite): # FUNÇÃO CONSTUTORA
        self.__numero = numero    #ATRIBUTO
        self.__titular = titular  #ATRIBUTO
        self.__saldo = saldo  #ATRIBUTO
        self.__limite = limite    #ATRIBUTO
        
    def extrato(self):  # METODO MOSTRAR EXTRATO
        print(f'O titular é {self.__titular}, sua conta é {self.__numero}, seu saldo: {self.__saldo} e seu limite é de: {self.__limite}')

    def deposita(self, valor):  # METODO DEPOSITAR VALOR
        self.__saldo += valor
        
    def __pode_sacar(self, valor_a_sacar):
        valor_disponivel_a_sacar = self.__saldo + self.__limite
        return valor_a_sacar <= valor_disponivel_a_sacar
        
    def sacar(self, valor):   # METODO SACAR VALOR
        if (self.__pode_sacar(valor)):
            self.__saldo -= valor
        else:
            print(f'O valor {valor} passou o limite!')
    
    def transferir(self, valor, destino):   # METODO TRANSFERIR
        self.sacar(valor)
        destino.deposita(valor)
        
    def get_saldo(self):    # "GET" Me devolve o valor atribuido à chave que voce envia como argumento para o método.
        return self.__saldo

    def get_titular(self):
        return self.__titular
    
    def get_limite(self):
        return self.__limite
    
    def set_limite(self, limite):   # "SET" Permitem as operações de adição, atualização e remoção de elementos.
        self.__limite = limite
    
    @staticmethod  
    def codigos_bancos():
        return {'BB': '001', 'CAIXA': '104', 'BRADESCO': '237'}
    
'''
Métodos estáticos:
Estamos criando umas contas com dicionário com os bancos: Brasil, Caixa e bradesco, que cada um possui um código, independe da conta, faz sentido acessá-lo sem termos um objeto da classe Conta.

    @staticmethod
    def codigos_bancos():
        return {'BB':'001', 'Caixa':'104', 'Bradesco':'237'}
    
Teste o código, crie uma conta e tente sacar um valor acima do limite mais o seu saldo, por exemplo:

    >>> from conta import Conta
    >>> Conta.codigo_banco()
    '001'
    >>> Conta.codigos_bancos()
    {'Caixa': '104', 'BB': '001', 'Bradesco': '237'}
'''
        
'''
Agora que vimos as propriedades, crie-os no lugar dos getters da classe Conta. Por exemplo, no lugar do get_saldo, teremos:

    @property
    def saldo(self):
        return self.__saldo

Da mesma forma, crie uma propriedade para o setter do atributo limite:

    @limite.setter
    def limite(self, limite):
        self.__limite = limite
        
No Python Console, dentro do próprio PyCharm, teste o código, crie uma conta e acesse o valor de algum atributo, utilizando somente o seu nome, por exemplo:

    >>> from conta import Conta
    >>> conta = Conta(123, "Nico", 55.5, 1000.0)
    Construindo objeto ... <conta.Conta object at 0x7f82af89d048>
    >>> conta.limite
    1000.0
    
Do mesmo jeito, altere o valor do atributo limite, deve funcionar como se você estivesse acessando-o diretamente:

    >>> from conta import Conta
    >>> conta = Conta(123, "Nico", 55.5, 1000.0)
    Construindo objeto ... <conta.Conta object at 0x7f82af89d048>
    >>> conta.limite = 2000.0
    >>> conta.limite
    2000.0
'''