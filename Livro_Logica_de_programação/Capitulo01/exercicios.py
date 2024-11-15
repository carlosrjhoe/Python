senhoras = ['Branca', 'Rosa', 'Violeta']
cores = ['branca', 'rosa', 'violeta']


def mostrar_vestidos():
    """Exercicio 1.1"""
    for senhora in senhoras:
        for cor in cores:
            if senhora != cor:
                if senhora == 'Rosa' and cor != 'rosa':
                    print(f'{senhora} está vestindo {cor}.')
                if senhora == 'Branca' and cor != 'branca':
                    print(f'{senhora} está vestindo {cor}.')
                if senhora == 'Violeta' and cor != 'violeta':
                    print(f'{senhora} está vestindo {cor}.')


def atravessar_rio():
    """RExercio 1.2"""
    print("1. O homem leva o bode para a outra margem.")
    print("2. O homem volta sozinho para a margem inicial.")
    print("3. O homem leva o lobo para a outra margem.")
    print("4. O homem traz o bode de volta para a margem inicial.")
    print("5. O homem leva o maço de alfafa para a outra margem.")
    print("6. O homem volta sozinho para a margem inicial.")
    print("7. O homem leva o bode para a outra margem.")

    print("\nTodas as cargas foram atravessadas com segurança!")


def torre_hanoi(n, origem, destino, auxiliar):
    if n == 1:
        print(f'Mova o disco 1 da haste {origem} para a haste {destino}')

    print(f'Mova o disco {n} da haste {origem} para a haste {destino}')

    torre_hanoi(n-1, origem, auxiliar, destino)
    torre_hanoi(n-1, auxiliar, destino, origem)


if __name__ == '__main__':
    torre_hanoi(3, 'A', 'C', 'B')
    