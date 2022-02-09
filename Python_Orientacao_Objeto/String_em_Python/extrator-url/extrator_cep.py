endereco = 'endereco = Rua das flores 72, apartamento 1002, Laranjeiras, Rio de Janeiro, 54515110'

import re
'''Regular Expression -- RegEx'''


padrao = re.compile('[0-9]{5}[-]?[0-9]{3}')
'''Encontar um padrão em uma string'''
busca = padrao.search(endereco)
if busca:
    cep = busca.group()
    print(cep)