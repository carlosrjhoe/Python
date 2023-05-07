inventario = {
    'rope': 1,
    'torch': 6,
    'gold coin': 42,
    'dagger': 1,
    'arrow': 12
}

def mostrarInventario(inventario):
    print("Inventario:")
    total_itens = 0
    for i, j in inventario.items():
        print(f"{i} - {str(j)}")
        total_itens = total_itens + j
    print(f"Total de intens: {total_itens}")

if __name__ == "__main__":
    mostrarInventario(inventario)