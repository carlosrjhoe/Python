class ContaCorrente:
    '''Definindo uma classe'''
    
    def __init__(self, codigo):
        '''Definindo um construtor'''
        self.codigo = codigo
        self.saldo = 0
    
    def deposita(self, valor):
        '''Definindo um metodo depositar'''
        self.saldo += valor
        
    def __str__(self):
        '''Definindo  uma representação de uma string'''
        return f"[>>Codigo {self.codigo} Saldo {self.saldo}<<]"
    
carlos = ContaCorrente(101)
carlos.deposita(250)
mayara = ContaCorrente(123)
mayara.deposita(300)

contas = [carlos, mayara]

depositos = [carlos.saldo, mayara.saldo]
for conta in contas:
    print(conta)
