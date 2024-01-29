cod, qtd = input().split()
cod, qtd = int(cod), int(qtd)
if cod == 1:
    print(f'Total: R$ {qtd*4.0:.2f}')
elif cod == 2:
    print(f'Total: R$ {qtd*4.5:.2f}')
elif cod == 3:
    print(f'Total: R$ {qtd*5.0:.2f}')
elif cod == 4:
    print(f'Total: R$ {qtd*2.0:.2f}')
elif cod == 5:
    print(f'Total: R$ {qtd*1.5:.2f}')