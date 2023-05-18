from time import sleep

def contagemRegressiva(final, total):
    print('Contagem regressiva...')
    while final <= 10:
        print(f'{total}')
        sleep(2)
        total -= 1
        final = total
        if total == -1:
            print('Contagem encerrada!')
            break

if __name__ == '__main__':
    final = 0
    total = 10
    contagemRegressiva(final, total)