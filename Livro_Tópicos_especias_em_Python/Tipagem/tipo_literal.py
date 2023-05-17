from typing import Literal

"""No corpo da função usuario( ) é criada toda uma estrutura condicional onde de acordo com a entrada é feita uma validação do tipo de dado de saída em Literal, reforçando que somente é permitido como dado retornado ‘logado’ ou ‘deslogado’, qualquer outra string diferente destas repassada como parâmetro para função usuario( ) irá exibir em tela ‘Status inválido’ para o usuário.

Feltrin, Fernando. Tópicos Especiais em Python - Fernando Feltrin . Edição do Kindle. """

def usuario(user: str) -> Literal['logado', 'deslogado']:
    if user == 'logado':
        print('Logado no sistema')
    elif user == 'deslogado':
        print('Deslogado no sistema')
    elif user != 'logado' and user != 'deslogado':
        print('Status inválido')

if __name__ == '__main__':
    usuario('logado')
    usuario('deslogado')
    usuario('OI')