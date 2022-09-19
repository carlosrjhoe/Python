class Verifica_clientes:
    
    
    def __init__(self) -> None:
        
        self.clientes = {
            'Carlos': 81995419951,
            'Mayara': 81987949484,
        }
        
        texto = 'Programa que ira verificar se o número de telefone consta em um banco de dados'
        print(f'{"#"*len(texto)}')
        print(f'{texto.center(len(texto))}')
        print(f'{"#"*len(texto)}')
        
        self.novo_cliente = ''
        self.nome = ''
        self.telefone = ''
        
    def verificar_cliente_no_banco_de_dados(self):
        self.novo_cliente = input('Digite o nome do cliente: ').title()
        if self.novo_cliente in self.clientes.keys():
            print(f'{self.novo_cliente} já existe na base de dados')
            self.novo_cliente = input(f'Digite o nome do cliente: ')
        else:
            print(f'{self.novo_cliente} não está cadastrado.')
            print('Digite novamente o nome a ser cadastrado:')
            self.nome = input(f'Digite seu nome: ')
            self.telefone = str(input('Digite o telefone: '))
            self.clientes.__setitem__(self.nome, self.telefone)
        print(self.clientes)
