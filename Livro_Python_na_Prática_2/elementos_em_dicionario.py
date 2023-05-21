"""Crie um simples mecanismo que valida a inserção de elementos em um dicionário, verificando se o elemento a ser adicionado ao mesmo já existe no dicionário atual.
"""

def adicionar_novo_cliente(clientes):
    novo_cliente = input('Digite o nome do cliente: ')

    if novo_cliente in clientes.keys():
        print(f'{novo_cliente} já existe na base de dados.')
        novo_cliente = input('Digite o nome do cliente: ')
    else:
        print(f'Para inserir {novo_cliente} a base de dados, precisa de um número de telefone:')
        clientes.__setitem__(novo_cliente, str(input('Digite o telefone: ')))
    print(clientes)
        

if __name__ == '__main__':
    clientes = {
        'carlos':'81977776666',
        'mayara':'81999998888',
        'neto':'81988887777',
        'luna':'81966665555'
    }
    adicionar_novo_cliente(clientes)