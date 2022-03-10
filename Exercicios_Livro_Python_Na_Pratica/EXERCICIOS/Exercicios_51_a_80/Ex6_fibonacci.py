from urllib import response


def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
num = int(input('Digite um numero para encontrar seu fibonacci: '))
resposta = fibonacci(num-1)
print(resposta)