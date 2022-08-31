with open('pi_digits.txt') as objeto_arquivo:
    conteudo = objeto_arquivo.read()
    print(f'{conteudo.strip()}')