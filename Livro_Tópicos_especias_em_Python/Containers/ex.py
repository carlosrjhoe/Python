def desempacotar(args):
    '''Embora não exista de fato algo como *args na declaração de uma variável, o marcador “ * “ aqui também é usado, para sinalizar ao interpretador esta propriedade do desempacotamento a ser realizado. ​Por meio das respectivas funções print( ) exibimos em tela os conteúdos das variáveis primeiros e ultimo, e como esperado, os dados foram desempacotados da tupla original e separados de acordo com a regra do marcador.'''
    primeiro,*intermediario, ultimo = args

    print(f'O primeiro número é: {primeiro}')
    print(f'Os números intermediários são: {intermediario}')
    print(f'O último é: {ultimo}')

if __name__ == '__main__':
    numeros = (1,2,3,4,5,6,7,8,9,10)
    desempacotar(numeros)

    # O primeiro número é: 1
    # Os números intermediários são: [2, 3, 4, 5, 6, 7, 8, 9]
    # O último é: 10