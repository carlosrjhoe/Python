def verificar_numeros(lista):
    for num in range(3):
        num = float(input('Digite um número: '))
        lista.append(num)

def media_aritmetica(lista):
    media = sum(lista) / len(lista)
    print(f'Média aritimética = {media:.1f}')

if __name__ == '__main__':
    lista = []
    verificar_numeros(lista)
    media_aritmetica(lista)