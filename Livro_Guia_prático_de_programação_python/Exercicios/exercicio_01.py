'''
    Escreva um código que: 
    1) Armazena o peso de José na variável peso_jose e o peso de Maria na variável peso_maria.
    2) Calcula a soma dos pesos dos dois e armazena o resultado na variável soma_pesos.
    3) Imprima a soma dos pesos, contida na variável soma_pesos.
'''

def soma_pesos(peso_1, peso_2):
    peso_total = peso_1 + peso_2
    return peso_total

if __name__ == '__main__':
    peso_1 = 80
    peso_2 = 55
    print(soma_pesos(peso_1, peso_2))