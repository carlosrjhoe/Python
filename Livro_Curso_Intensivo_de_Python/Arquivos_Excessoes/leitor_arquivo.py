# with open('pi_digits.txt') as objeto_arquivo:
#     conteudo = objeto_arquivo.read()
#     print(f'{conteudo.rstrip()}')

file_name = 'pi_digits.txt'
with open(file_name) as ob:
    for line in ob:
        print(line)