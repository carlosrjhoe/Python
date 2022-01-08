# CRIANDO UMA FUNÇÃO
def fahrenheit(x):
    return (x * (9/5)) + 32

x = float(input('Digite uma temperatura em (C°): '))
print(f'A temperatura digitada em {x}C°, é igual a {fahrenheit(x)}F°')