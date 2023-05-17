"""– Crie uma estrutura de código de validação de uma senha digitada pelo usuário. Após inserida a senha, a mesma deve ser inspecionada em busca das seguintes características: Conter entre 6 e 16 caracteres, conter ao menos uma letra minúscula, conter ao menos um número, conter ao menos uma letra maiúscula e conter ao menos um caractere especial ($#@*!&).
"""

import re

def cadastrar_senha():
    senha = input('Insira sua senha: ')
    x = True

    while x:
        if len(senha) < 6 or len(senha) > 16:
            print(f'A senha deve conter entre 6 e 16 caracteres.')
            break
        elif not re.search('[a-z]', senha):
            print('A senha deve ter ao menos uma letra minúcula.')
            break
        elif not re.search('[0-9]', senha):
            print('A senha deve conter ao menos um número.')
            break
        elif not re.search('[@#$%&*!]', senha):
            print('A senha deve conter ao menos um caractere especial')
            break
        elif re.search('\s', senha):
            break
        else:
            print('Senha cadastrada com sucesso!!!')
            x = False
            break
    if x:
        print('Senha invalida!!!')

if __name__ == '__main__':
    cadastrar_senha()