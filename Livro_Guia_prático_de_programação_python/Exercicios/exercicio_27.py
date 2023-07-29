def gerar_numeros_primos():
    primos = [index for index in range(1, 101) if index % 2 != 0]
    return primos

if __name__ == "__main__":
    print(gerar_numeros_primos())