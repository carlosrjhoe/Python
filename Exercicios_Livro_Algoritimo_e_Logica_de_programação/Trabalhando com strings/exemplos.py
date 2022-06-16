""" Listagem 7.1 – Alteração de uma string"""
# S = 'Alô mundo'
# print(S[0])

"""Listagem 7.2 – Convertendo uma string em lista"""
# S = list('Olá Mundo')
# S[0] = 'a'
# print(S)

# s = ''.join(S)
# print(s)

"""7.1 Verificação parcial de strings"""

nome = 'Carlos Roberto Conceição Junior'
# print(nome.startswith('Carlos'))
# print(nome.startswith('Roberto'))
# print(nome.endswith('Junior'))
# print(nome.endswith('Conceição'))

""" Listagem 7.5 – Pesquisa de palavras em uma string usando in"""

# print('Carlos' in nome)
# print('Junior' in nome)
# print('Mayara' in nome)

"""Listagem 7.6 – Pesquisa de palavras em uma string usando not in"""

print('Carlos' not in nome)
print('Mayara' not in nome)