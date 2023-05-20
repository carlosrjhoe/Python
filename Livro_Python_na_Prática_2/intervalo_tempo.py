"""Escreva um programa que recebe do usuário um intervalo de tempo em anos, retornando a partir desta informação o número de ocorrências de um dia específico (nesse caso, as segundas-feiras) dentro de um dia específico do mês (nesse caso, no dia primeiro de cada mês do intervalo de tempo previamente definido).
"""

from datetime import datetime

def intervalo_de_tempo():
    segundas = 0
    meses = range(1, 13)

    ano_inicio = int(input('Digite o ano inicial: '))
    ano_fim = int(input('Digite o ano final: '))
    
    intervalo = []
    intervalo.append(ano_inicio)
    intervalo.append(ano_fim)

    for ano in range(intervalo[0], intervalo[1]+1):
        for mes in meses:
            if datetime(ano, mes, 1).weekday() == 0:
                segundas += 1

    print(f'Entre {intervalo[0]} e {intervalo[1]} existem {segundas} segundas-feiras no primeiro dia do mês.')

if __name__ == '__main__':
    intervalo_de_tempo()