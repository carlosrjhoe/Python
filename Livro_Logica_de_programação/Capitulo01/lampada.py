senhoras = ['Branca', 'Rosa', 'Violeta']
cores = ['branca', 'rosa', 'violeta']


def mostrar_vestidos():
    """Mostrar as senhoras e seus respectivos vestidos"""
    for senhora in senhoras:
        for cor in cores:
            if senhora != cor:
                if senhora == 'Rosa' and cor != 'rosa':
                    print(f'{senhora} está vestindo {cor}.')
                if senhora == 'Branca' and cor != 'branca':
                    print(f'{senhora} está vestindo {cor}.')
                if senhora == 'Violeta' and cor != 'violeta':
                    print(f'{senhora} está vestindo {cor}.')


if __name__ == '__main__':
    mostrar_vestidos()