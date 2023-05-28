'''Supondo que temos um dicionário, representando usuários de um sistema, onde cada item do dicionário é um usuário descrito por seu id, nome, sobrenome e e-mail, exiba em tela de forma estruturada (exatamente como escrita no corpo do código) o conteúdo desse dicionário.
'''
from pprint import pprint

def nova_formatacao(lista):
    pprint(data)
    return

if __name__ == '__main__':
    data = {'usuario': [
        {'id':1,
        'nome': 'carlos',
        'sobreNome': 'conceição',
        'e-mail': 'carlosrjhoe@gmail.com',
        },
        {'id':2,
        'nome': 'mayara',
        'sobreNome': 'ramos',
        'e-mail': 'mayararamos@gmail.com',
        },
        {'id':3,
        'nome': 'carlos',
        'sobreNome': 'neto',
        'e-mail': 'carlosrcneto@gmail.com',
        },
        {'id':4,
        'nome': 'luna',
        'sobreNome': 'ramos',
        'e-mail': 'lunaramos@gmail.com',
        },
    ]}

    nova_formatacao(data)