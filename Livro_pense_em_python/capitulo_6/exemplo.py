# def verifica(x, y):
#     if x > y:
#         return 1
#     elif x == y:
#         return 0
#     else:
#         return -1

from math import sqrt
from math import pi
from turtle import distance

def area(radius):
    a = pi * radius**2
    return a

def distance(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    soma_quadrados = dx**2 + dy**2
    resultado = sqrt(soma_quadrados)
    return resultado

def circle_area(x1, y1, x2, y2):
    radius = distance(x1, y1, x2, y2)
    result = area(radius)
    return result


    
# def hipotenusa(a, b):
#     """
#         Calcula o comprimento da hipotenusa de um triângulo 
#         retângulo dados os comprimentos dos outros dois lados.
#     """
#     return sqrt(a**2 + b**2)

if __name__ == '__main__':
    num_1, num_2, num_3, num_4 = 3, 5, 6, 8
    print(distance(num_1, num_2, num_3, num_4))
    print(circle_area(num_1, num_2, num_3, num_4))