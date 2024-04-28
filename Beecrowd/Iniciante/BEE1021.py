def main():
    reais, centavos = map(int, input('').split('.'))
    centavos = centavos + reais*100
    NOTAS = [100, 50, 20, 10, 5, 2]
    MOEDAS = [100, 50, 25, 10, 5, 1]
    
    print('NOTAS:')
    for nota in NOTAS:
        print(f'{centavos//(nota*100)} nota(s) de R$ {nota}.00')
        centavos = centavos%(nota*100)

    print('MOEDAS:')
    for moeda in MOEDAS:
        print(f'{centavos//moeda} moeda(s) de R$ {moeda//100}.{moeda%100:02}')
        centavos = centavos % moeda
if __name__ == '__main__':
    main()