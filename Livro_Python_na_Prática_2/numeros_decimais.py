'''Como bem sabemos, operações matemáticas em Python realizadas a partir de valores numéricos muito próximos tendem a gerar números com casas decimais, valores em casas decimais normalmente “arredondados” por questões de performance. Porém, em computação científica pode ser necessário números com grande número de casas decimais pois estes valores, quanto mais extensos, simbolizam maior precisão. Realize a simples soma de dois valores 0.1 e 0.2, retornando um terceiro número de no mínimo 20 casas decimais.
'''

import decimal as deci

def transforma_numero_em_decimal():
    numero = deci.Decimal(0.1) + deci.Decimal(0.2)
    return numero

if __name__ == '__main__':
    print(f'{transforma_numero_em_decimal()}')