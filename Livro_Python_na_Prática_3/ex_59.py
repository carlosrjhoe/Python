"""Implemente um gerador de números primos.:"""

def primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

def gerador():
    numero = 2
    while True:
        if primo(numero):
            yield numero
        numero += 1

if __name__ == "__main__":
    for _ in range(10):
        print(next(gerador()))