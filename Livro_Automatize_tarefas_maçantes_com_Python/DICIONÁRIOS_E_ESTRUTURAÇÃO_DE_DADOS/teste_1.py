familia = {
    "Carlos": "03 de Novembro de 1985",
    "Mayara": "04 de Janeiro de 1985",
    "Neto": "31 de Outubro de 2015",
    "Luna": "07 de Outubro de 2017",
}

while True:
    nome = input("Digite seu nome ou [Q] para sair: ").title()
    if nome == "Q":
        break
    if nome in familia:
        print(f"{familia[nome]} é o aniversario de {nome}")
    else:
        print(f"Não tenho informações de aniversário de {nome}")
        novo_aniversario = input("Qual é o dia do seu aniversário? ")
        
        familia[nome] = novo_aniversario
        
        print("Banco de dados de aniversário atualizado")
