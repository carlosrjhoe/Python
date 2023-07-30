def tabela_precos():
    VALOR = 1.99
    for index in range(1, 101):
        resultado = index*VALOR
        print(f'Item: {index} - R${resultado:.2f}')

if __name__ == "__main__":
    tabela_precos()