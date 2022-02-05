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
    
    def sacar(self, valor):   # METODO SACAR VALOR
        if valor > self.__saldo:
            print('Saldo insuficiente')
        else:
            self.__saldo -= valor
    
    def transferir(self, valor, destino):   # METODO TRANSFERIR
        self.sacar(valor)
        destino.deposita(valor)
        