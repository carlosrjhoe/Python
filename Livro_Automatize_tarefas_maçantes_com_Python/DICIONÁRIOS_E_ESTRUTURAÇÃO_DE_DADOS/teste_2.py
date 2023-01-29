familia = {
    "Carlos": "03 de Novembro de 1985",
    "Mayara": "04 de Janeiro de 1985",
    "Neto": "31 de Outubro de 2015",
    "Luna": "07 de Outubro de 2017",
}

for i, j in familia.items():
    # Nesse caso, um loop for faz uma iteração, e fazendo atribuição multipla do dicionário
    print(f"Nome: {i}, Nascimento: {j}")

    
for i in familia.keys():
    # Nesse caso, um loop for faz uma iteração, percorrendo cada chave do dicionário
    print(i)

    
for i in familia.values():
    # Nesse caso, um loop for faz uma iteração, percorrendo cada um dos valores do dicionário
    print(i)