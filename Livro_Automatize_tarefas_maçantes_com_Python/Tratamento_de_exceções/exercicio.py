# Sequência de Collatz

def collatz(numero):
  if numero % 2 == 0:
    return numero // 2
  else:
    return 3 * numero + 1

numero = int(input('Digite um numero: '))
print(collatz(2))