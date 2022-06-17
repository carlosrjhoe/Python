""" Listagem 8.1 – Definição de uma nova função"""

# def soma(a,b):
#     print(a+b)
    
# soma(2,9)
# soma(7,8)
# soma(10,15)

"""Listagem 8.2 – Definição do retorno de um valor"""

# def soma(a,b):
#     return a+b

# print(soma(2,9))

"""Listagem 8.3 – Retornando se valor é par ou não"""

# def epar(x):
#     return x % 2 == 0

# print(epar(8))
# print(epar(5))

"""Listagem 8.4 – Reutilização da função épar em outra função"""

# def par_ou_impar(x):
#     if epar(x):
#         return 'Par'
#     else:
#         return 'Ipar'

# print(par_ou_impar(4))
# print(par_ou_impar(9))

""" Listagem 8.5 – Pesquisa em uma lista"""

# L = [10,20,25,30]

# def pesquise(lista, valor):
#     for x, e in enumerate(lista):
#         if e == valor:
#             return x
#     return None

# print(pesquise(L, 25))
# print(pesquise(L, 27))

"""Listagem 8.6 – Cálculo da média de uma lista"""

# def soma(L):
#     total = 0
#     for e in L:
#         total += e
#     return total

# def media(L):
#     return (soma(L)/len(L))

# print(soma(L))
# print(media(L))

""" Listagem 8.9 – Cálculo do fatorial"""

def fatorial(num):
    fat = 1
    while num > 1:
        fat *= num
        num -= 1
    return fat

print(fatorial(4))