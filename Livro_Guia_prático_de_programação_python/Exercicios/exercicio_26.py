lista = []
def criar_lista():
    for index in range(1, 6):
        num = int(input(f'Informe o {index}° número: '))
        lista.append(num)
    return lista

def soma_lista():
    return sum(lista)

def media_lista():
    return (sum(lista) / len(lista))

def resumo():
    print(f'A soma dos números foi de: {soma_lista()}')
    print(f'A média dos números foi de: {media_lista():.2f}')

if __name__ == "__main__":
    criar_lista()
    resumo()

    # Informe o 1° número: 1
    # Informe o 2° número: 2
    # Informe o 3° número: 3
    # Informe o 4° número: 4
    # Informe o 5° número: 5
    # A soma dos números foi de: 15
    # A média dos números foi de: 3.00