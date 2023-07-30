par = []
impar = []
def resumo():
    for index in range(1, 4):
        num  = int(input(f'Digite o {index}° número: '))
        if num % 2 == 0:
            par.append(num)
        else:
            impar.append(num)

    print(f'Números pares: {len(par)}')
    print(f'Números impares: {len(impar)}')

    
if __name__ == "__main__":
    resumo()