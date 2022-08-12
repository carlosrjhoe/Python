palavra = 'Preenchendo um dicionário com dados de entrada do usuário.'
print('#'*len(palavra))
print(f'{(palavra.center(len(palavra)))}')
print('#'*len(palavra))

respostas = {} # Criar um dicionário vazio
sondagem_ativa = True

# Define uma flag para indicar que a enquete está ativa
while sondagem_ativa:
    #  Pede o nome da pessoa e a resposta
    nome = input('Escreva seu nome: ')
    resposta = input('Qual montanha você gostaria de escalar um dia? ')
    # Armazena uma resposta no dicionário
    respostas[nome] = resposta
    # Descobre se outra pessoa vai responder a mesma enquete
    repetir = input('Você gostaria de deixar outra pessoa responder[sim/nao]? ')
    if repetir == 'nao':
        sondagem_ativa = False
# A enquete foi concluida. Mostrar os resultados
print('Resultados da enquete:')
for nome, resposta in respostas.items():
    print(f'{nome.title()} gostaria de escalar {resposta.title()}')
    
print(respostas)