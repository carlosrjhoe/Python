lista = set()
while True:
    try:
        lista.add(input())
    except (EOFError, KeyboardInterrupt):
        break
lista = set(lista)
print(len(lista))