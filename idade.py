texto = 'IDADE'
print('*' * 45)
print('{:^45}'.format(texto))
print('*' * 45)

idade_str = input("Digite sua idade: ")
idade = int(idade_str)

if (idade >= 18):
    print("Você é maior de idade.")
else:
    if (idade <= 12):
        print("Você é uma criança.")
    elif (idade >= 12):
        print("Você é um adolescente.")
