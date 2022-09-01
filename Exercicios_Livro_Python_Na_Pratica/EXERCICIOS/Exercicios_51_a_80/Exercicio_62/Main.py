from medicos import Medicos
from cadastro_plano_de_saude import usuarios

texto = 'Exercicio - 63 (Medicos)'
print('#' * len(texto))
print(f'{texto.center(len(texto))}')
print('#' * len(texto))

usuario = input('Digite seu numero de cadastro: ')

if usuario in usuarios.keys():
    
    if usuario == '001':
        usuario = 'carlos'
        print(f'Bem-vindo {usuario.title()}')
    elif usuario == '002':
        usuario = 'mayara'
        print(f'Bem-vinda {usuario.title()}')
    elif usuario == '003':
        usuario = 'neto'
        print(f'Bem-vindo {usuario.title()}')
    elif usuario == '004':
        usuario = 'luna'
        print(f'Bem-vinda {usuario.title()}')
        
    menu = input('Deseja marcar uma consulta[S ou N]? ').upper()
    
    if menu == 'N':
        print(f'Ok, Obrigado.')
    else:
        medico = int(input('Gostaria de marcar com qual Médico: \n 1: Maria Rosiclé \n 2: Ana Lúcia\nOpcção: '))

        if medico == 1:
            print(f'Sua consulta com a Dra {Medicos[0]} foi marcada com sucesso!')
        elif medico == 2:
            print(f'Sua consulta com a Dra {Medicos[1]} foi marcada com sucesso!')
    
else:
    print('Usuário desconhecido!')
        
        