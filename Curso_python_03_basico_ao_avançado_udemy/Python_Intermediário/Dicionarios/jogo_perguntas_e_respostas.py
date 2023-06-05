def jogo_perguntas_e_respostas(lista):
    for pergunta in lista:
        print(f"Pergunta: {pergunta['Pergunta']}")
        print(f"Opções: {pergunta['Opções']}")
        resposta = input(f'Resposta: ')
        if not pergunta['Resposta'] == resposta:
            print('Você Errou!')
        else:
            print('Você acertou!')

if __name__ == '__main__':
    perguntas = [
        {
        'Pergunta': 'Quanto é 2+2',
        'Opções': ['1', '4', '3', '2', '5', '10'],
        'Resposta': '4',
        },
        {
        'Pergunta': 'Quanto é 5*5',
        'Opções': ['50', '100', '1000', '200', '25', '10'],
        'Resposta': '25',
        },
        {
        'Pergunta': 'Quanto é 10/2',
        'Opções': ['1', '8', '3', '2', '5', '10'],
        'Resposta': '5',
        },
    ]

    jogo_perguntas_e_respostas(perguntas)


# >>> Pergunta: Quanto é 2+2
# >>> Opções: ['1', '4', '3', '2', '5', '10']
# >>> Resposta: 4
# >>> Você acertou!
# >>> Pergunta: Quanto é 5*5
# >>> Opções: ['50', '100', '1000', '200', '25', '10']
# >>> Resposta: 50
# >>> Você Errou!
# >>> Pergunta: Quanto é 10/2
# >>> Opções: ['1', '8', '3', '2', '5', '10']
# >>> Resposta: 5
# >>> Você acertou!