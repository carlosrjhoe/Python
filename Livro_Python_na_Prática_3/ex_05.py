"""5 – Dada uma lista de strings, crie um dicionário usando list comprehension que armazene cada string como chave e seu comprimento como valor. Imprima o dicionário produzido no console:"""

def criar_dicionario(lista_strings):
    """dictionary comprehension - Para criar um dicionário onde cada string da lista lista_strings é usada como chave e seu comprimento (obtido com a função len()) como valor. A variável string itera sobre cada string da lista lista_strings a cada ciclo de repetição até que não existam mais elementos iteráveis."""
    
    dicionario = {string.title(): len(string) for string in lista_strings}
    print(f'Nomes e números de letras: {dicionario}')


if __name__ == '__main__':
    lista_strings = ['python', 'java', 'c++', 'javascript', 'ruby']
    criar_dicionario(lista_strings)

    # >>> Nomes e números de letras: {'Python': 6, 'Java': 4, 'C++': 3, 'Javascript': 10, 'Ruby': 4}