def quadrado(lista_de_numeros):
   lista_quadrada = []
   for numero in lista_de_numeros:
      lista_quadrada.append(numero ** 2)

   return lista_quadrada

def cubo(lista_de_numeros):
   lista_cubo = []
   for numero in lista_de_numeros:
      lista_cubo.append(numero ** 3)

   return lista_cubo

lista_de_valores = []

for valor in range(10):
   lista_de_valores.append(
      int(input('Digite um numero: '))
   )

dicionario = {
   'lista padrão' : lista_de_valores,
   'lista quadrada': quadrado(lista_de_valores),
   'lista cúbica': cubo(lista_de_valores)
}
print(dicionario)