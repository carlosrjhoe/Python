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
    categoria = input(f'Digite o nome da categoria do restaurante: {nome_restaurante} ')
    dados_restaurante = {'nome': nome_restaurante, 'categoria': categoria, 'status': False}
    restaurantes.append(dados_restaurante)
    print(f'{nome_restaurante} cadastrado com sucesso.')
    
    voltar_ao_menu_principal()
    
def alternar_status_restaurante():
    exibir_sub_titulos('Alternando estado do restaurante.')
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar STATUS: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['status'] = not restaurante['status']
            msg = f'O restaurante {nome_restaurante} foi ativado com sucesso.' if restaurante['status'] else f'O restaurante {nome_restaurante} foi desativado com sucesso.'
            print(msg)

    if not restaurante_encontrado:
        print('O restaurante não foi encontrado')
            
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
            alternar_status_restaurante()
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