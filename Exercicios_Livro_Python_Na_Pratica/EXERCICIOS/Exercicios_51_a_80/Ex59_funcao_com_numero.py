'''Criar uma função de números de parâmetros indefinidos, que realiza a soma dos números passados como parametros, independente da quantidade de números'''

def soma(*args): # Função
    num = 0
    for valordigitado in args:
        num += valordigitado
    print(f'O resultado da soma é {num}')
    
soma(18, 43, 99, 1, 20, 40) # Parametro