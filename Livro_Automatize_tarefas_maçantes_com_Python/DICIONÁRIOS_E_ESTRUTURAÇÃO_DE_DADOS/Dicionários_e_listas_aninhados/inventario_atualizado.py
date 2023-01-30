inventario = {'gold coin': 42, 'rope': 1}
saqueDragao = ['gold coin', 
               'dagger', 
               'gold coin', 
               'gold coin', 
               'ruby'
            ]

def adicionarAoInventário(inventario, saqueDragao):
    for i, j in inventario.items():
        for i in saqueDragao:
            inventario[i] = inventario[i] + 1
    print(inventario)

            
        
if __name__ == '__main__':
    adicionarAoInventário(inventario ,saqueDragao)