def verificar_numeros(lista):
    for num in range(2):
        num = int(input('Digite um número: '))
        lista.append(num)

def media_aritmetica(lista):
    media = sum(lista) / 2
    print(f'Média aritimética = {media}')

if __name__ == '__main__':
    lista = []
    verificar_numeros(lista)
    media_aritmetica(lista)