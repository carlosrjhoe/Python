"""
    2 – Crie uma estrutura de código que lê o conteúdo interno de uma função, retornando o número de identificação da função e o número de variáveis que a mesma possui alocadas em memória.
"""

def minha_funcao():
    x = 1
    y = 2
    nome = 'carlos'
    lista = [1,2,3]
    return f'{x}, {y}, {nome}, {lista}'

if __name__ == '__main__':
    var_locias = minha_funcao.__code__.co_nlocals
    print(f'A função {minha_funcao} possui {var_locias} variáveis.')
    print(minha_funcao())