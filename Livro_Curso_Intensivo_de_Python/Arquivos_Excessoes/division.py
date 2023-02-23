"""Se o código no bloco try causar um erro, o interpretador procurará um bloco except cujo erro coincida com aquele levantado e executará o código desse bloco."""
try:
    print(5/0)
except ZeroDivisionError:
    print('Você não pode dividir por zero')
