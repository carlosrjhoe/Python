"""Exercício 8.7 Defina uma função recursiva que calcule o maior divisor comum
(M.D.C.) entre dois números a e b, onde a > b"""

def mdc(a,b):
    if b == 0:
        return a
    return mdc(b, a % b)

print(f'MDC de [10 e 5] --> {mdc(10,5)}')
print(f'MDC de [32 e 24] --> {mdc(32,24)}')
print(f'MDC de [5 e 3] --> {mdc(5,3)}')