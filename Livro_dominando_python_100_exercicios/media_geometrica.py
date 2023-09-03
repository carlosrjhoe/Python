from math import pow

def verificar_numeros(lista):
    for num in range(1, 4):
        num = float(input(f'Digite o {num}° número: '))
        lista.append(num)
    return lista

def media_geometrica():
    num_1, num_2, num_3 = lista
    media = pow(num_1*num_2*num_3, 1/3)
    return media

def inf():
    print(f'A média geométrica dos números é: {media_geometrica()}')
    
if __name__ == '__main__':
    lista = []
    verificar_numeros(lista)
    inf()