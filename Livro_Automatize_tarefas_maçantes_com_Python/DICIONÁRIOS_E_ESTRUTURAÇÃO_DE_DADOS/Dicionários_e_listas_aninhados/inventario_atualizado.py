inventario = {'gold coin': 42, 'rope': 1,}
saqueDragao = ['gold coin', 
               'dagger', 
               'gold coin', 
               'gold coin', 
            ]

def mostra(inventario):
    total = 0
    print("Inventario:")
    for i, j in inventario.items():
        total = total + j
    print(total)

if __name__ == "__main__":
    mostra(inventario)