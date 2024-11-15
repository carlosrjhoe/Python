def soma(num_1, num_2):
    resultado = num_1 + num_2
    return resultado


def subtracao(num_1, num_2):
    resultado = num_1 - num_2
    return resultado


def multiplicacao(num_1, num_2):
    resultado = num_1 * num_2
    return resultado


def divisao(num_1, num_2):
    resultado = num_1 / num_2
    return int(resultado)


if __name__ == "__main__":
    print(soma(4, 2))
    print(subtracao(4, 2))
    print(multiplicacao(4, 2))
    print(divisao(4, 2))
