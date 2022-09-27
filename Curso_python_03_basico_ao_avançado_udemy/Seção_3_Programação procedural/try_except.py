from re import A


try:
    a = 1/0
    print(a)
except (NameError) as erro:
    print('Erro do desenvolvedor.')
except Exception as erro:
    print('Ocorreu um erro inesperado.')
except IndexError as erro:
    print('Erro de indice')
else:
    print('Bora continuar...')
finally:
    print('Perfeito')
    