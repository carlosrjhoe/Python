# Listagem 3.16 – Entrada de dados

# num = input('Digite um numero: ')
# print(num)

nome = input("Digite seu nome: ")
if nome.isdigit():
  print('entrada de dados não válida.')
else:
  print(f"Você digitou, {nome}")
  print(f"Olá, {nome}")