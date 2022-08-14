texto = 'Preenchendo um dicionário com dados de entrada do usuário.'
print('#'*len(texto))
print(f'{(texto.center(len(texto)))}')
print('#'*len(texto))


"""
    Criar um dicionário vazio
    Define uma flag para indicar que a enquete está ativa
    Pede o nome da pessoa e a resposta
    Armazena uma resposta no dicionário
    Descobre se outra pessoa vai responder a mesma enquete
    A enquete foi concluida. Mostrar os resultados
"""

respostas = {} 
sondagem_ativa = True

while sondagem_ativa:
    nome = input('Escreva seu nome: ')
    resposta = input('Qual montanha você gostaria de escalar um dia? ')
    respostas[nome] = resposta
    repetir = input('Você gostaria de deixar outra pessoa responder[sim/nao]? ')
    if repetir == 'nao':
        sondagem_ativa = False
print('Resultados da enquete:')
for nome, resposta in respostas.items():
    print(f'{nome.title()} gostaria de escalar {resposta.title()}')
