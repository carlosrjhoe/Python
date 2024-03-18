import os

restaurantes = [
    {'nome': 'Praça', 'categoria': 'japonesa', 'status': False},
    {'nome': 'Pizza Suprema', 'categoria': 'Italiana', 'status': True},
    {'nome': 'Cantina', 'categoria': 'Brazileirinho', 'status': True}
]

def exibindo_programa():
    print("""
    ░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
    ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
    ╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
    ░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
    ██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
    ╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░  
    """)
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Ativar restaurante')
    print('4. Sair\n')

def finalizar_app():
    exibir_sub_titulos('4. Saindo do programa...')

def opcao_invalida():
    print('Opção inválida!\n')
    voltar_ao_menu_principal()

def exibir_sub_titulos(texto):
    os.system('cls')
    print(texto)
    print()

def voltar_ao_menu_principal():
    input('\nDigite uma tecla para voltar ao menu principal ')
    main()

def cadastrar_novo_restaurante():
    exibir_sub_titulos('Cadastro de novos restaurantes')
    nome_restaurante = input('Nome do restaurante? ')
    restaurantes.append(nome_restaurante)
    print(f'{nome_restaurante} cadastrado com sucesso.')
    
    voltar_ao_menu_principal()
    

def listar_restaurantes():
    exibir_sub_titulos('Listando restaurantes:')
    for restaurante in restaurantes:
        rest_nome = restaurante['nome']
        rest_categoria = restaurante['categoria']
        rest_status = restaurante['status']
        print(f'{rest_nome} | {rest_categoria} | {rest_status}')

    voltar_ao_menu_principal()

def exibir_opcoes():

    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            print('Ativar restaurante')
        elif opcao_escolhida == 4:
            print('Finalizar app')
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()
        
        
def main():
    os.system('cls')
    exibindo_programa()
    exibir_opcoes()

if __name__ == "__main__":
    main()