num = int(input())
for _ in range(num):
    lista = input().split()
    lista = sorted(set(lista))
    print(' '.join(str(item) for item in lista))