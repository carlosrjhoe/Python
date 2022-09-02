numeros = (33, 1987, 2020)
dados = {'nome': 'carlos', 'profissao': 'líder manutencao'}

def identificacao(*args, **kwargs):
    print(f'{args}\n{kwargs}')
    
identificacao(*numeros, **dados)