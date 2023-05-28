'''Uma vez que temos as frações 1/4 e 5/8, realize a soma dessas frações, exibindo em tela detalhadamente seus numeradores, denominadores e o próprio resultado da soma.
'''

from fractions import Fraction

def verificar_1_fracao(num_1, num_2):
    fracao_1 = Fraction(num_1, num_2)
    print(f'Fração: {fracao_1}')
    print(f'Numerador da 1º Fração: {fracao_1.numerator}')
    print(f'Denominador da 1º Fração: {fracao_1.denominator}')
    return fracao_1

def verificar_2_fracao(num_1, num_2):
    fracao_2 = Fraction(num_1, num_2)
    print(f'Fração: {fracao_2}')
    print(f'Numerador da 2º Fração: {fracao_2.numerator}')
    print(f'Denominador da 2º Fração: {fracao_2.denominator}')
    return fracao_2

def soma_das_fracoes(def_1, def_2):
    soma = Fraction(def_1) + Fraction(def_2)
    print(f'Soma das fraçoes: {soma}')
    return soma

if __name__ == '__main__':
    verificar_1_fracao(1,4)
    verificar_2_fracao(5,8)
    soma_das_fracoes(verificar_1_fracao(1,4), verificar_2_fracao(5,8))        