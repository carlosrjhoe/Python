def descrever_animais(raca_animal, nome_animal):
    """Exibe informação sobre o animal de estimação"""
    return f'Eu tenho um {raca_animal}.\nMeu {raca_animal} e seu nome é {nome_animal.title()}.'
    
print(descrever_animais('yorkshire', 'tufik'))