magicians = ["Grande Houdini", "Fu-Manchu", "Richiardi Jr", "Jasper Maskelyne", "Dai Vernon", "David Blaine", "Siegfried Fischbacher", "David Copperfield", "Anjo Criss"]

modifiked_magicians = []

def show_magicians(magicians):
    print("Mostrando lista de magicos!")
    for magician in magicians:
        print(f"{magician}")
    print("################################################")

def modifiked(magicians, modifiked_magicians):
    while magicians:
        current_magician = magicians.pop()
        modifiked_magicians.append(current_magician)

def show_modifiked_magicians(modifiked_magicians):
    print("Mostrando lista de magicos modificados!")
    for magician in modifiked_magicians:
        print(f"O Grande {magician}")
    print("################################################")

if __name__ == "__main__":
    show_magicians(magicians)
    modifiked(magicians, modifiked_magicians)
    show_modifiked_magicians(modifiked_magicians)
