"""8 – Dadas duas listas de strings, use das funções zip( ) e dict( ) para criar um dicionário que use os elementos da primeira lista como chaves e os elementos da segunda lista como valores. Exiba em tela o conteúdo do novo dicionário:"""

def criar_dicionario(a, b):
    dicionario = dict(zip(a, b))
    print(f'Dicionário: {dicionario}')

    
if __name__ == "__main__":
    chaves = ['nome', 'idade', 'cidade', 'pais']
    valores = ['carlos','37', 'bahia', 'brasil']
    criar_dicionario(chaves, valores)

# >>> Dicionário: {'nome': 'carlos', 'idade': '37', 'cidade': 'bahia', 'pais': 'brasil'}