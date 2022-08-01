""" 61 - Escreva um programa que retorna o número de Fibonacci: Sendo o número de Fibonacci um valor iniciado em 0 ou em 1 onde cada termo subsequente corresponde à soma dos dois anteriores."""

from urllib import response


def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
numero = int(input('Digite um número para encontar seu Fibonaci: '))
resposta = fibonacci(numero-1)
print(resposta)