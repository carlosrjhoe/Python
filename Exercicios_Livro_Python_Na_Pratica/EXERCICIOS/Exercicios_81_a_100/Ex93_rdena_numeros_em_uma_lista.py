def ordena_lista(lista):
    for i in range(1, len(lista)):
        valor = lista[i]
        indice = i - 1
        while indice >= 0:
            if valor < lista[indice]:
                lista[indice + 1], lista[indice] = lista[indice], lista[indice + 1]
                indice -= 1
            else:
                break
    return lista

lista_1 = ordena_lista([9,0,3,4,6,5,7,8,2,1])
print(lista_1)