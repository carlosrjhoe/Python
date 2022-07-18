class Conta:
    '''Definindo uma classe'''
    
    def __init__(self, codigo):
        '''Definindo um construtor'''
        self._codigo = codigo
        self._saldo = 0
        '''Atribuindo atributos privados com "self._"'''
    
    def deposita(self, valor):
        '''Definindo um metodo depositar'''
        self._saldo += valor
        
    def __str__(self):
        '''Definindo  uma representação de uma string'''
        return f"[>>Codigo {self._codigo} Saldo {self._saldo}<<]"
    
class ContaCorrente(Conta):
    '''Definindo uma herança da classe "Conta"'''
    def passa_o_mes(self):
        self._saldo -= 2
        '''A primeira tira só dois reais quando passa um mês'''
        
class ContaPoupanca(Conta):
    
    def passa_o_mes(self):
        self._saldo *= 1.01
        self._saldo -= 3
        '''Dá 1% do saldo e depois tira três reais toda vez que passa um mês'''
        
conta_mayara = ContaPoupanca(102)
conta_mayara.deposita(1000)
conta_mayara.passa_o_mes()

conta_carlos = ContaPoupanca(101)
conta_carlos.deposita(1010)
conta_carlos.passa_o_mes()
'''Criando contas'''

contas = (conta_carlos, conta_mayara)
'''Adicionando as contas em uma tupla'''

for conta in contas:
    conta.passa_o_mes() # duck typing
    print(conta)
    '''Agora, eu quero passar por todas as contas, então "for conta in contas:" e eu vou passar o mês, "conta.passa_o_mes()". Não importa se dentro da lista eu tenho "ContaCorrente ou ContaPoupanca", o que importa é que tenha o "passa_o_mes()"'''