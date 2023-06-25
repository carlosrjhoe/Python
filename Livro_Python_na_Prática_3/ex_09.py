"""9 – Dada uma lista de strings, use a função map( ) e uma função lambda para criar uma nova lista contendo cada string da lista original com a primeira letra em maiúsculas e depois faça outra com todoas as letras em caixa alta. Imprima a nova lista no console:"""

def cria_lista(lista):
    """Função map( ) para aplicar a função lambda x: x.capitalize( ) em cada elemento da lista lista_strings. A função lambda recebe cada string x da lista e aplica o método capitalize( ) para deixar a primeira letra em maiúscula. Em seguida, usamos a função list( ) para converter o resultado de volta em uma lista e armazenamos na variável nova_lista."""
    
    nova_lista = list(map(lambda x: x.capitalize(), lista))
    print(f'Nova lista: {nova_lista}')
    return

def criar_lista_caixa_alta(lista):
    nova_lista = list(map(lambda x: x.upper(), lista))
    print(f'Nova Lista caixa alta: {nova_lista}')
    return

if __name__ == "__main__":
    lista_strings = ['python', 'java', 'c++', 'javascript', 'ruby']
    cria_lista(lista_strings)
    criar_lista_caixa_alta(lista_strings)

    # >>> Nova lista: ['Python', 'Java', 'C++', 'Javascript', 'Ruby']
    # >>> Lista caixa alta: ['PYTHON', 'JAVA', 'C++', 'JAVASCRIPT', 'RUBY']