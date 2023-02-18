familia = ['carlos', 'mayara', 'neto', 'luna']

def mostrar_familia(familia):
    for id, nome in enumerate(familia):
        print(f'{id+1} - {nome.title()}')

def verificar_parente(familia):
    print('carlos' in familia)
    print('lucia' in familia)
    return


if __name__ == '__main__':
    mostrar_familia(familia)
    verificar_parente(familia)