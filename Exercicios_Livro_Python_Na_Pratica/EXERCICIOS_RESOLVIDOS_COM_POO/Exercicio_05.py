"""5 - Crie uma variável nome e atribua para a mesma um nome digitado pelo usuário:

Feltrin, Fernando. Python na Prática: Aprenda Python Através de Exercícios Comentados (p. 23). Uniorg. Edição do Kindle. """

nome = ''
def pergutar_nome(nome):
    nome = input("Digite seu nome: ")
    print(f"Seu nome é {nome.title()}")
    return

pergutar_nome(nome)

    
