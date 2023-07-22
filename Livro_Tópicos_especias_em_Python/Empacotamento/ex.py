def identificacao(*args, **kwargs):
    print(f'{args}\n{kwargs}')

if __name__ == '__main__':
    numeros = (37,38,1987,2022,19.19,100000)
    dados = {'Nome': 'Carlos', 'Profissao': 'Encarregado'}

    identificacao(*numeros, **dados)