nomes = ["carlos","mayara","neto","luna",]

nome = input("Qual seu nome: ")
if nome not in nomes:
    print(f"Não te conheço {nome}. ")
else:
    print(f"Oie! {nome}")