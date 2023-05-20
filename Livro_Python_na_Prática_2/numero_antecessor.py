"""Uma prática comum é para certos contextos gerar listas, dicionários, ou qualquer outro tipo de contêiner de dados com alguns valores padrão ou gerados a partir de algum critério. Nessa linha de raciocínio, crie um gerador de dicionário que, com um dado inteiro n fornecido pelo usuário, retorna um dicionário composto por todos números antecessores ao número n e seus valores quando elevados ao quadrado.
"""
from math import pow

def perguntaNumero():
    numero = int(input('Digite um número: '))
    dicionario = {}
    for i in range(1, numero + 1):
        dicionario[i] = i * i
    print(f'{dicionario}')

if __name__ == '__main__':
    perguntaNumero()