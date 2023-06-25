"""1 – A partir de uma sequência de números digitados pelo usuário, separados por vírgula, converta tal sequência numérica em uma lista, exibindo em tela seu conteúdo:"""


def converter_sequencia():
    numeros = input('Insira uma sequência de números separados por vírgula: ')
    lista_numeros = [int(numero) for numero in numeros.split(',')]
    print(f'Lista de números: {lista_numeros}')
    return
    
if __name__ == '__main__':
    converter_sequencia()

    # >>>Insira uma sequência de números separados por vírgula: 2,3,4,5,6,7,8,93,12
    # >>>Lista de números: [2, 3, 4, 5, 6, 7, 8, 93, 12]