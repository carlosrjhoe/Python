def solicitar_nota():
    VERIFICAR = [1, 2, 3, 4, 5]
    while True:
        nota = int(input('Informe uma nota entre [0-5]: '))
        if nota not in VERIFICAR:
            print('Valor inválido')
        else:
            break
    print('Fim')


if __name__ == "__main__":
    solicitar_nota()