nome_2 = "Mayara"  # Variável no escopo global


def imprimirNome(nome_1):
    nome_2 = "Neto"  # Variável no escopo local
    print(f"{nome_1}")
    print(f"{nome_2}")


if __name__ == "__main__":
    print(f"{nome_2}")
    imprimirNome("Carlos")
