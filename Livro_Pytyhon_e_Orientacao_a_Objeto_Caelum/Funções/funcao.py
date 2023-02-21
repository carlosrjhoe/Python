import math

def boas_vindas():
    print('Olá, seja bem vindo ao meu programa!!!')
    print('Espero que você tenha uma boa experiência...')

def elevar_ao_cubo(numero):
    """Função composta, com parâmetros"""
    return math.pow(numero, 2)

def mostrar_info(*args):
    """Função composta, com *args: Args os mesmos serão tratados como uma lista"""
    for i in args:
        print(f'{i} + {i}')

def mostrar_info_2(**kwargs):
    """Função composta, com *kwargs: Kwargs espera que, como num dicionário, sejam atribuidos chaves:valores"""
    for i, f in kwargs.items():
        print(f'{i}: {f}')
    
    
if __name__ == '__main__':
    boas_vindas()
    print(elevar_ao_cubo(3))
    mostrar_info('Olá mundo')
    mostrar_info_2(nome='carlos', idade= 37, formacao = ['Analista de Sistemas', 'Técnico em mecânica'])