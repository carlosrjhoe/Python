"""Escreva uma estrutura de validação que verifica se o endereço de um site foi digitado corretamente. O endereço escrito deve ser em formato de domínio brasileiro (terminado em .com.br) e para o processo de validação não pode ser usado expressões regulares.
"""

def verica_site():
    endereco = input('Digite o endereço completo de seu site: ')

    while ((endereco.startswith('www.') and endereco.endswith('.com.br'))) != True:
        print('O endereço deve incluir "www" e ".com.br"')
        endereco = input('Digite seu site novamente: ')

    print(f'{endereco} é um endereço válido!')

if __name__ == '__main__':
    verica_site()
        