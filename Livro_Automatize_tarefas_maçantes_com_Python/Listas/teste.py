# lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(lista)
# print(lista[-2])
# print(lista[1:6])
# print(len(lista))
# lista[5] = 11
# print(lista)
# del lista[6]
# print(lista)

nomes_dos_gatos = []

while True:
    nome = input(f'Digite o nome do {str(len(nomes_dos_gatos)+1)} gato: ')
    if nome == "":
        break
    nomes_dos_gatos = nomes_dos_gatos + [nome]
print("Os nome dos gatos são:")
for i in nomes_dos_gatos:
    print(i)

        