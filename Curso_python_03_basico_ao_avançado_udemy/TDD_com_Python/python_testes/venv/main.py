from Calculadora import soma

try:
    print(f'{soma(10, "20")}')
except AssertionError as erro:
    print(f"Conta invalida {erro}")

print("OI")