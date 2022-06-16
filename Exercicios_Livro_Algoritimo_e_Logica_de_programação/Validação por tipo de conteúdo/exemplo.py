"""Listagem 7.21 – Validação de strings por seu conteúdo"""

# s = '125'
# print(s.isalnum())
# p = 'Olámundo'
# print(p.isalpha())

"""Listagem 7.22 – Validação de strings com números"""

# print('77.7'.isdigit())

""" Listagem 7.23 – Diferenciação de isnumeric de isdigit"""

# um_terco = '\u2153'
# nove_biteriano = '\u0f29'
# print(nove_biteriano.isdigit())
# print(nove_biteriano.isnumeric())

""" Listagem 7.24 – Verificação de maiúsculas e minúsculas"""

s = 'ABC'
p = 'abc'
e = 'aBc'

print(e.isupper())
print(e.islower())