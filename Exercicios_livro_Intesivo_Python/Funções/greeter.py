def greeter_user(username):
    """Comprimentar usuário"""
    print(f'Hello {username.title()}')

greeter_user('carlos')
greeter_user('mayara')
greeter_user('neto')
greeter_user('luna')

def display_message():
    print('Estou apredendo sobre funções em python!')

display_message()

def favorite_book(livro):
    print(f'Um dos meus livros favorios é: {livro}.')

if __name__ == '__main__':
    favorite_book('Alice no pais das maravilhas.')
    favorite_book('Pense em python')
    favorite_book('Python e Django.')
    favorite_book('Código limpo.')
