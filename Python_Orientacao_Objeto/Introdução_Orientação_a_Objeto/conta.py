class Conta:    # CLASS

    def __init__(self, numero, titular, saldo, limite): # FUNÇÃO CONSTUTORA
        self.numero = numero    #ATRIBUTO
        self.titular = titular  #ATRIBUTO
        self.saldo = saldo  #ATRIBUTO
        self.limite = limite    #ATRIBUTO
        
    def extrato(self):  # METODO MOSTRAR EXTRATO
        print(f'O titular é {self.titular}, sua conta é {self.numero}, seu saldo: {self.saldo} e seu limite é de: {self.limite}')

    def deposita(self, valor):  # METODO DEPOSITAR VALOR
        self.saldo += valor
    
    def sacar(self, valor):   # METODO SACAR VALOR
        if valor > self.saldo:
            print('Saldo insuficiente')
        else:
            self.saldo -= valor