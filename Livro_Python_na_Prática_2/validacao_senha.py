"""– Crie uma estrutura de código de validação de uma senha digitada pelo usuário. Após inserida a senha, a mesma deve ser inspecionada em busca das seguintes características: Conter entre 6 e 16 caracteres, conter ao menos uma letra minúscula, conter ao menos um número, conter ao menos uma letra maiúscula e conter ao menos um caractere especial ($#@*!&).
"""

import re

def cadastrarSenha():
    senha = input('Insira sua senha: ')
    x = True # variável de controle
    
    while x:
        if len(senha) < 6 or len(senha) > 16:
            # Verifica se o tamanho de senha é menor que 6 ou maior que 16
            print(f'A senha deve conter entre 6 e 16 caracteres.')
            break
        elif not re.search('[a-z]', senha):
            # Verifica se o retorno não contem caracteres minúsculos de A até Z.
            print('A senha deve ter ao menos uma letra minúcula.')
            break
        elif not re.search('[0-9]', senha):
            # Verifica se o retorno não contem números de 0 até 9.
            print('A senha deve conter ao menos um número.')
            break
        elif not re.search('[@#$%&*!]', senha):
            # Verifica se o retorno não contem caracteres especiais.
            print('A senha deve conter ao menos um caractere especial')
            break
        elif re.search('\s', senha):
            # Verifica no retorno não contem espaços em branco.
            break
        else:
            print('Senha cadastrada com sucesso!!!')
            x = False
            break
    if x:
        print('Senha invalida!!!')

if __name__ == '__main__':
    cadastrarSenha()