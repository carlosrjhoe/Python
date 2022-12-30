def pergunta():
    num1 = int(input("Digite um número: "))
    num2 = int(input("Digite outro número: "))

    print(f"A soma de {num1} e {num2} = {num1 + num2}")
    print(f"A subtração de {num1} e {num2} = {num1 - num2}")
    print(f"A multiplicação de {num1} e {num2} = {num1 * num2}")
    print(f"A divisão de {num1} e {num2} = {num1 / num2}")


if __name__ == "__main__":
    pergunta()