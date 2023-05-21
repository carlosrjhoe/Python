"""Escreva um programa que procura um certo dado / valor a partir de múltiplos dicionários, conforme dado inserido pelo usuário. Os dicionários em questão devem possuir itens domésticos representados com nome e preço. Retorne ao usuário o item consultado, de qual dicionário foi extraído e seu valor em reais.
"""

from collections import ChainMap

def buscar_itens(cabecalho, cozinha, sala, quarto, banheiro):
    objeto = ChainMap(cozinha, sala, quarto, banheiro)
    item = input('Digite um item a ser buscado: ').capitalize()

    if item in cozinha.keys():
        print(cabecalho['texto_1'])
        print(f'O valor de {item} é de R${objeto[item]:.2f}')
    elif item in sala.keys():
        print(cabecalho['texto_2'])
        print(f'O valor de {item} é de R${objeto[item]:.2f}')
    elif item in quarto.keys():
        print(cabecalho['texto_3'])
        print(f'O valor de {item} é de R${objeto[item]:.2f}')
    elif item in banheiro.keys():
        print(cabecalho['texto_4'])
        print(f'O valor de {item} é de R${objeto[item]:.2f}')
    else:
        print(cabecalho['texto_5'])

if __name__ == '__main__':
    cabecalho = {
        'texto_1' : 'Informação extraída a partir do dicionário [cozinha]:',
        'texto_2' : 'Informação extraída a partir do dicionário [sala]:',
        'texto_3' : 'Informação extraída a partir do dicionário [quarto]:',
        'texto_4' : 'Informação extraída a partir do dicionário [banheiro]:',
        'texto_5' : 'O item buscado não consta em nenhum dicionário.'
    }
    cozinha = {'Fogão': 470.00,'Geladeira': 1100.00,'Forno Micro-ondas': 399.00} 
    sala = {'Sofá': 799.00,'Estante': 499.00}
    quarto = {'Cama': 1049.00,'Roupeiro': 899.00,'Criado Mudo': 224.00}
    banheiro = {'Pia': 459.00,'Vaso': 499.00,'Lixeira': 49.00}

    buscar_itens(cabecalho, cozinha, sala, quarto, banheiro)