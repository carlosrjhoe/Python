def soma(fator_1, fator_2):
    return  fator_1 + fator_2

def subtracao(fator_1, fator_2):
    return fator_1 - fator_2

def multiplicacao(fator_1, fator_2):
    return fator_1 * fator_2

def divisao(fator_1, fator_2):
    return fator_1 / fator_2
    
def resulmo():
    fator_1 = int(input('Digite o primeiro número: '))
    fator_2 = int(input('Digite o segundo número: '))
    print(f'A soma dos números {fator_1} e {fator_2} = {soma(fator_1, fator_2)}')
    print(f'A subitração dos números {fator_1} e {fator_2} = {subtracao(fator_1, fator_2)}')
    print(f'A multiplicação dos números {fator_1} e {fator_2} = {multiplicacao(fator_1, fator_2)}')
    print(f'A divisão dos números {fator_1} e {fator_2} = {divisao(fator_1, fator_2)}')

if __name__ == '__main__':
    resulmo()