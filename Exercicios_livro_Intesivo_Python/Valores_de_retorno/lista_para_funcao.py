def greet_user(names):
    """Exibir uma saudação simpçes para cada usuário"""
    for name in names:
        print(f"Hello {name.title()}")
    return

if __name__ == '__main__':
    usuarios = ['carlos', 'mayara', 'neto', 'luna']
    greet_user(usuarios)