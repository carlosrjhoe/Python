inventario = {'gold coin': 42, 'rope': 1, 'ruby': 1, 'dagger': 1}
saqueDragao = ['gold coin', 
               'dagger',
               'dagger',
               'gold coin', 
               'gold coin',
            ]

def info(inventario, saqueDragao):

    for key in inventario.items():
        total = 0
        for key in saqueDragao:
            if key == 'gold coin':
                total = total + 1
    inventario['gold coin'] += total
 
    print("Inventário:")
    quantidade = 0
    for nome, qtd in inventario.items():
        print(f"{qtd} - {nome}")
        quantidade = quantidade + qtd
    print(f"Número total de itens: {quantidade}")

if __name__ == '__main__':
    info(inventario, saqueDragao)