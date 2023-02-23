# with open('pi_digits.txt') as objeto_arquivo:
#     conteudo = objeto_arquivo.read()
#     print(f'{conteudo.rstrip()}')

file_name = 'pi_digits.txt'
with open(file_name) as ob:
    lines = ob.readlines()

pi_string = ''
"""criamos uma variável pi_string para armazenar os dígitos de pi"""
for line in lines:
    """criamos um laço que acrescenta cada uma das linhas de dígitos em pi_string removendo o caractere de quebra de linha"""
    pi_string += line.rstrip()

print(pi_string[:10])
"""exibiremos as 10 primeiras casas decimais"""

# print(len(pi_string))