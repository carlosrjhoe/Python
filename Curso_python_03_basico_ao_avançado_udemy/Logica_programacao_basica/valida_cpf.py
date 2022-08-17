cpf = '06019931447'
novo_cpf = cpf[:9]

for index in range(19):
    if index > 8:
        index -= 9
    print(index)