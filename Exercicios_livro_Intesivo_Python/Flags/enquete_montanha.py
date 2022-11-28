respostas = {}

# Define uma flag para indicar que a enquete está ativa
votação_ativa = True

while votação_ativa:
    # Pedir o nome da pessoa
    nome = input('\nQual é seu nome? ').title()
    resposta = input('Qual montanha você gostaria de escalar algum dia? ')

    # Armazena a resposta no dicionário
    respostas[nome] = resposta.title()

    # Perguntar se vai ter outra pessoa para responder a enquete, caso a resposta seja não, a enquete está encerrada.
    repetir = input('Você gostaria de deixar outra pessoa responder(s/n)? ')
    if repetir == 'n':
        votação_ativa = False

print('\n--- RESULTADO DA INQUETE ---')
for nome, resposta in respostas.items():
    print(f'{nome} gostaria de escalar {resposta} algum dia.')