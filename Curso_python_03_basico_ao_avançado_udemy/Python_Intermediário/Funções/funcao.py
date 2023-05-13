def dadosComArgumentosDefault(nome="Nome não informado", idade="Idade não informada"):
    print(f"Dados:\nNome: {nome}\nIdade: {idade}")

def dadosSemArgumento(*args):
    print(f"Dados:\nNome: {args[0]}\nIdade: {args[1]}")

if __name__ == "__main__":
    dadosSemArgumento("Mayara", 38)
    dadosComArgumentosDefault("Carlos", 37)
    dadosComArgumentosDefault()
    dadosComArgumentosDefault("Neto", 7)
    dadosComArgumentosDefault("Luna", 5)