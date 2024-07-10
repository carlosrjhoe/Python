# def verifica(x, y):
#     if x > y:
#         return 1
#     elif x == y:
#         return 0
#     else:
#         return -1

# from math import sqrt
# from math import pi
# from turtle import distance

# def area(radius):
#     a = pi * radius**2
#     return a

# def distance(x1, y1, x2, y2):
#     dx = x2 - x1
#     dy = y2 - y1
#     soma_quadrados = dx**2 + dy**2
#     resultado = sqrt(soma_quadrados)
#     return resultado

# def circle_area(x1, y1, x2, y2):
#     radius = distance(x1, y1, x2, y2)
#     result = area(radius)
#     return result


    
# def hipotenusa(a, b):
#     """
#         Calcula o comprimento da hipotenusa de um triângulo 
#         retângulo dados os comprimentos dos outros dois lados.
#     """
#     return sqrt(a**2 + b**2)

# def is_divisible(x: int, y: int):
#     if x % y == 0: 
#         return True
#     else:
#         return False

def factorial(n: int):
    space = ' ' * (4 * n)
    print(f'{space} factorial {n}')
    """Padrão guardião do factorial"""
    # if not isinstance(n, int):
    #     print('Factorial is only defined for integers.')
    #     return None
    # elif n < 0:
    #     print('Factorial is not defined for negative integers.')
    #     return None
    # elif n == 0:
    if n == 0:
        print(f'{space} returning 1')
        return 1
    else:
        recurse = factorial(n-1)
        result = n * recurse
        print(f'{space} returning {result}')
        return result

# def fibonacci(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)
    
if __name__ == '__main__':
    print(factorial(4))