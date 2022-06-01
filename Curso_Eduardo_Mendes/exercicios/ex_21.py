def quadrado(lista_de_numeros):
    lista_resposta = []
    for numeros in lista_de_numeros:
        lista_resposta.append(numeros ** 2)
    return lista_resposta

def cubo(lista_de_numeros):
    lista_resposta = []
    for numeros in lista_de_numeros:
        lista_resposta.append(numeros ** 3)
    return lista_resposta

lista_valores = []

for valor in range(10):
    lista_valores.append(
        int(input('Fala um número ai: '))
    )
dicionario = {
    'lista padrão': lista_valores,
    'lista quadrada': quadrado(lista_valores),
    'lista cúbica': cubo(lista_valores)
}

print(dicionario)