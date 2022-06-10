"""3.1 – Nomes: Armazene os nomes de alguns de seus amigos em uma lista
chamada names. Exiba o nome de cada pessoa acessando cada elemento da lista,
um de cada vez"""

nomes = ['carlos', 'mayara', 'neto', 'luna']
print(nomes[0])
print(nomes[1])
print(nomes[2])
print(nomes[3])

""".
3.2 – Saudações: Comece com a lista usada no Exercício 3.1, mas em vez de
simplesmente exibir o nome de cada pessoa, apresente uma mensagem a elas. O
texto de cada mensagem deve ser o mesmo, porém cada mensagem deve estar
personalizada com o nome da pessoa"""

for nome in nomes:
    print(f'Olá {nome.title()}, seja bem vindo(a)')

"""3.3 – Sua própria lista: Pense em seu meio de transporte preferido, como
motocicleta ou carro, e crie uma lista que armazene vários exemplos. Utilize sua
lista para exibir uma série de frases sobre esses itens, como “Gostaria de ter uma
moto Honda”."""

