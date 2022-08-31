from medicos import Medicos

def consulta():
    menu = input('Deseja marcar uma consulta[S ou N]? ').upper()

    if menu == 'N':
        print(f'Ok, Obrigado.')
    else:
        nome = input('Qual o seu nome: ').title()
        medico = int(input('Gostaria de marcar com qual Médico: \n 1: Maria Rosiclé \n 2: Ana Lúcia\nOpcção: '))
        
        if medico == 1:
            print(f'Olá, {nome}. \nSua consulta com a Dra {Medicos[0]} foi marcada com sucesso!')
        elif medico == 2:
            print(f'Olá, {nome}. \nSua consulta com a Dra {Medicos[1]} foi marcada com sucesso!')
            
consulta()