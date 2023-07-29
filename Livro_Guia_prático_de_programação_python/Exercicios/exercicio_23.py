def cabecalho():
    print('VALOR JUROS\tVALOR TOTAL\tPARCELAS\tVALOR DAS PARCELAS')

def calculo_juros(juros, divida):
    for parcela, juro in juros.items():
        print(f'R${juro}\t\tR${(divida*juro)+divida:1.2f}\t{parcela}\t\tR${((divida*juro)+divida)/int(parcela):1.2f}')
    

if __name__ == '__main__':
    divida = float(input('Qual o valor da sua dívida: '))
    juros = {'1': 0.0, '3': 0.10, '6': 0.15, '7': 0.20, '9': 0.25}
    cabecalho()
    calculo_juros(juros, divida)