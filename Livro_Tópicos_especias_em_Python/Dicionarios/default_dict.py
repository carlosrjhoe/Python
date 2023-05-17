from collections import defaultdict

dicionario = defaultdict(int)
dicionario['Ano'] = 2023
dicionario['Mês'] = 5

def info():
    print(dicionario.items())
    print(dicionario['Dia'])
    print(dicionario['Mês'])

if __name__ == '__main__':
    info()