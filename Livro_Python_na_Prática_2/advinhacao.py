import random

def perguntarNumero(num_gerado, num_sorteado):
    while num_gerado != num_sorteado:
        num_sorteado = int(input('Digite um número entre [0-10]: '))
    print('Parabéns, você advinhou o número!')
    print(f'Número gerado: {num_gerado}')
        
if __name__ == '__main__':
    num_gerado, num_sorteado = random.randint(0, 11), 0
    perguntarNumero(num_gerado, num_sorteado)
    