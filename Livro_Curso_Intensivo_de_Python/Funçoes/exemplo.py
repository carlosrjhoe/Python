def bom_uso():
    """Exibe uma msg simples"""
    print('Olá mundo')
    
bom_uso()

def descricao(tipo_animal='cachorro', nome_animal='tufik'):
    """Exibe informações sobre um animal de estimação."""
    print(f'\nEu tenho um {tipo_animal.title()}.')
    print(f'Meu {tipo_animal.title()} seu nome é {nome_animal.title()}')

"""Várias chamadas de função"""

descricao() # Valores default
descricao('hamister', 'ig')