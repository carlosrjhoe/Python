from src.service.service_user import ServiceUser

if __name__ == "__main__":
    service = ServiceUser()

    # Teste com parâmetros inválidos
    print(service.add_user("Carlos", "Engenheiro"))  # Usuário adicionado com sucesso!
    # print(service.add_user("Carlos", ""))  # Erro: Nome e profissão devem ser strings não vazias.

    # Adicionando novos usuários
    # print(service.add_user("Carlos", "Engenheiro"))  # Usuário adicionado com sucesso!
    print(service.add_user("Carlos", "Designer"))  # Erro: Usuário com o nome 'Carlos' já existe.

    # Outro usuário
    # print(service.add_user("Ana", "Designer"))  # Usuário adicionado com sucesso!
    # print(service.add_user("Ana", "Engenheiro"))  # Usuário adicionado com sucesso!

    # Deletar usuário
    # print(service.del_user('Carlos'))
    # print(service.del_user('Ana'))

    # Update usuário
    # print(service.update_user('Carlos', 'Cozinheiro'))

    # já existe para atualizar
    # print(service.get_user_by_name('Carlos'))

    #
    print(service.get_user_by_name('Carlos'))
