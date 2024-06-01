# def verifica(x, y):
#     if x > y:
#         return 1
#     elif x == y:
#         return 0
#     else:
#         return -1

from math import sqrt

# def distance(x1, y1, x2, y2):
#     dx = x2 - x1
#     dy = y2 - y1
#     soma_quadrados = dx**2 + dy**2
#     resultado = sqrt(soma_quadrados)
#     return resultado

def hipotenusa(a, b):
    """
        Calcula o comprimento da hipotenusa de um triângulo 
        retângulo dados os comprimentos dos outros dois lados.
    """
    return sqrt(a**2 + b**2)

if __name__ == '__main__':
    a, b = 5, 8
    print(f'o comprimento da hipotenusa de um triângulo retângulo: {hipotenusa(a, b):.3f}')