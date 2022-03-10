'''Crie uma função que recebe parâmetros tanto por justaposição (*args) quanto nomeados (**kwargs)'''

def identificacao(*args, **kwargs):
    for n in args:
        nome = n
        print(f'Nome: {n}')
        
        for k, v in kwargs.items():
            idade = k
            sexo = v
            print(f'Nome: {nome}, {idade}, {sexo}')
            
identificacao('fernando', idade = 33, sexo = 'M')