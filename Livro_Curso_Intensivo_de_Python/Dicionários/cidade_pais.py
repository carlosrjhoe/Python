"""8.6 – Nomes de cidade: Escreva uma função chamada city_country() que
aceite o nome de uma cidade e seu país. A função deve devolver uma string
formatada assim:
"Santiago, Chile"
Chame sua função com pelo menos três pares cidade-país e apresente o valor
devolvido"""

def cidades_pais(cidade, pais):
    print(f'{cidade}, {pais}')

while True:
    print('Digite o nome de sua Cidade e o Pais:')
    cidade = input('Me fale o nome de sua Cidade: ').title()
    if cidade == 'Q':
        break
    pais = input('Me fale o nome do seu Pais: ').title()
    if pais == 'Q':
        break

    cidades_pais(cidade, pais)