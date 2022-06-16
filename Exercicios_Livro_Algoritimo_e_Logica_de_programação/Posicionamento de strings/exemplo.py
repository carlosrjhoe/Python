""" Listagem 7.14 – Centralização de texto em uma string"""

# s = "tigre"
# print(s.center(21, '='))

""" Listagem 7.15 – Preenchimento de strings com espaços"""

# print(s.ljust(20, '-'))
# print(s.rjust(20, '-'))

""" Listagem 7.16 – Separação de strings"""

# nomes = 'Um tigre, dois tigres, três tigres'
# print(nomes.split(','))
# print(nomes.split(' '))

""" Listagem 7.17 – Quebra de strings de várias linhas"""

nomes = 'Um\ tigre\ dois\ tigres\ três\ tigres\n'
print(nomes.splitlines())