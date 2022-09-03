from time import sleep
texto = 'Jogo de perguntas e respostas'

print(f'{"#"*len(texto)}')
print(texto.center(len(texto)))
print(f'{"#"*len(texto)}')

perguntas = {
    'pergunta 1': {
        'pergunta': 'Quanto é 2+2?',
        'respostas': {
            'a': '1',
            'b': '8',
            'c': '4'
        },
        'resposta_certa': 'c'
    },
    'pergunta 2': {
        'pergunta': 'Quanto é 20-7?',
        'respostas': {
            'a': '18',
            'b': '9',
            'c': '13'
        },
        'resposta_certa': 'c'
    },
    'pergunta 3': {
        'pergunta': 'Quanto é 5*9?',
        'respostas': {
            'a': '45',
            'b': '36',
            'c': '72'
        },
        'resposta_certa': 'a'
    },
    'pergunta 4': {
        'pergunta': 'Quanto é 15/4?',
        'respostas': {
            'a': '3',
            'b': '5,7',
            'c': '3,75'
        },
        'resposta_certa': 'c'
    },
    'pergunta 5': {
        'pergunta': 'Quanto é 5+37?',
        'respostas': {
            'a': '37',
            'b': '42',
            'c': '49'
        },
        'resposta_certa': 'b'
    },
}

respostas_certas = 0

for pergunta, dados_pergunta in perguntas.items():
    print(f'{pergunta}: {dados_pergunta["pergunta"]}')
    
    print('Respostas:')
    for resposta, dados_resposta in dados_pergunta['respostas'].items():
        print(f'[{resposta}]: {dados_resposta}')
        
    resposta_usuario = input('Sua resposta: ')
    
    if resposta_usuario == dados_pergunta['resposta_certa']:
        print('Você acertou!!!!\n')
        respostas_certas += 1
    else:
        print('Você errou!!!!\n')
    
    sleep(1)


quantidade_de_perguntas = len(perguntas)
porcentagem_acerto = respostas_certas / quantidade_de_perguntas * 100

texto1 = 'Resultado'

print(f'{"#"*len(texto)}')
print(texto1.center(len(texto)))
print(f'{"#"*len(texto)}')
print(f'Você acertou {respostas_certas} questões.')
print(f'Sua porcentagem de acerto foi de {porcentagem_acerto}')