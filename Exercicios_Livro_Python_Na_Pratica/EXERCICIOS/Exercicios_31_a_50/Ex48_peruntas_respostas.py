base = {
    'pergunta01': {
        'pergunta':'Quanto é 4 x 4?',
        'alternativa':{'a':'12','b':'24','c':'16','d':'20'},
        'respostas_certa':'c'
    },
    'pergunta02': {
        'pergunta':'Quanto é 6 / 3?',
        'alternativa':{'a':'2.5','b':'3','c':'2','d':'1.5'},
        'respostas_certa':'c'
    }
}

respostas_certas = 0

for pkeys, pvalues in base.items():
    print(f'{pkeys}:{pvalues["pergunta"]}')
    
    for rkeys, rvalues in pvalues['alternativas'].item():
        print(f'[{'rkeys'}]:{'rvalues'}')
        
    resposta = input('Escolha uma alternativa: [a][b][c] ou [d]')
    
    if resposta == pvalues['respostas_certas']:
        print('Resposta correta0')
        respostas_certas += 1
    else:
        print('respostaIncorreta')