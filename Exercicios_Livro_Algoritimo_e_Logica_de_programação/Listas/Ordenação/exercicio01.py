"""Exercício 6.14 O que acontece quando a lista já está ordenada? Rastreie o programa
da listagem 6.44, mas com a lista L=[1,2,3,4,5]."""

# L=[1,2,3,4,5]

# fim = 5
# while fim > 1:
#     trocou = False
#     x = 0
#     while x < (fim-1):
#         if L[x] > L[x+1]:
#             trocou =True
#             temp = L[x]
#             L[x] = L[x+1]
#             L[x+1] = temp
#         x += 1
#     if not trocou:
#         break
#     fim -= 1
# for e in L:
#     print(e)
    
"""Exercício 6.15 O que acontece quando dois valores são iguais? Rastreie o programa
da listagem 6.44, mas com a lista L=[3,3,1,5,4]"""

L=[3,3,1,5,4]

fim = 5
while fim > 1:
    trocou = False
    x = 0
    while x < (fim-1):
        if L[x] > L[x+1]:
            trocou =True
            temp = L[x]
            L[x] = L[x+1]
            L[x+1] = temp
        x += 1
    if not trocou:
        break
    fim -= 1
for e in L:
    print(e)