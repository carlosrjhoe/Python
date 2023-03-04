import json

def get_stored_username():
    """Obtém o nome do usuário já armazenado se estiver disponível."""
    filename = 'usuario_2.json'
    try:
        with open(filename) as object_file:
            username = json.load(object_file)
            # ler as informações armazenadas em username.json 
    except FileNotFoundError:
        return None
    else:
        return username

def greet_user():
    username = get_stored_username()
    if username:
        print(f'Welcome back, {username}')
    else:
        username = input('What is your username: ').title()
        filename = 'usuario_2.json'
        with open(filename, 'w') as object_file:
            # Usei json.dump() para armazenar o nome do usuário e exibimos uma saudação.
            json.dump(username, object_file)
            # converte os objetos Python em objetos json apropriados
            print(f"We'll remember you when you come back, {username}!")

if __name__ == "__main__":
    greet_user()
