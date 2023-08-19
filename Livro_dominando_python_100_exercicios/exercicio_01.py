def soma(num_1, num_2):
    return num_1 + num_2

def subtracao(num_1, num_2):
    return num_1 - num_2

def multiplicacao(num_1, num_2):
    return num_1 * num_2

def divisao(num_1, num_2):
    return num_1 / num_2
    
def resulmo():
    print(f'A soma dos números {num_1} e {num_2} = {soma(num_1, num_2)}')
    print(f'A subitração dos números {num_1} e {num_2} = {subtracao(num_1, num_2)}')
    print(f'A multiplicação dos números {num_1} e {num_2} = {multiplicacao(num_1, num_2)}')
    print(f'A divisão dos números {num_1} e {num_2} = {divisao(num_1, num_2)}')

    
if __name__ == '__main__':
    num_1 = int(input('Digite o 1º número: '))
    num_2 = int(input('Digite o 2º número: '))
    resulmo()