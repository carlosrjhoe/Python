magicians = ["Grande Houdini", "Fu-Manchu", "Richiardi Jr", "Jasper Maskelyne", "Dai Vernon", "David Blaine", "Siegfried Fischbacher", "David Copperfield", "Anjo Criss"]

modified_magicians = []

def show_magicians(magicians):
    print("Mostrando lista de magicos!")
    for magician in magicians:
        print(f"{magician}")
    print("################################################")

def modify(magicians, modified_magicians):
    while magicians:
        current_magician = magicians.pop()
        modified_magicians.append(current_magician)

def show_modified_magicians(modified_magicians):
    print("Mostrando lista de magicos modificados!")
    for magician in modified_magicians:
        print(f"O Grande {magician}")
    print("################################################")

if __name__ == "__main__":
    show_magicians(magicians)
    modify(magicians, modified_magicians)
    show_modified_magicians(modified_magicians)
