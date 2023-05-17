"""
    3 – Uma vez que temos a lista [“maçã”, “banana”, “laranja”, “abacate”, “pêssego”], busque extrair o segundo e o quarto elemento da lista de forma ainda mais reduzida e otimizada do que quando utilizamos list comprehension.
"""

lista = ['maçã', 'banana', 'laranja', 'abacate']

from operator import itemgetter

minhas_frutas = list(itemgetter(1,3)(lista))
print(f'{minhas_frutas}')