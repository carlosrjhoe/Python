"""13 – Crie uma expressão regular que valide se uma string é um número de telefone válido no formato (DDD) XXXXX-XXXX ou (DDD) XXXX-XXXX. Teste a expressão regular com alguns exemplos de números de telefone válidos e inválidos, exibindo em tela via print( ) o retorno destes testes:"""

import re

def verifica_telefone(base_dados_telefone):
    telefone_regex = r'^\(\d{2}\)\d{4,5}-\d{4}$'
    for num in base_dados_telefone:
        if re.match(telefone_regex, num):
            """para verificar se cada número de telefone corresponde à expressão regular telefone_regex."""
            print(f'{num} - é um telefone válido.')
        else:
            print(f'{num} - não é um telefone válido.')

if __name__ == '__main__':
    base_dados_telefone = [
        '(811)1234-5678','(21)91234-5678','(14)9123-4567',
        '(11)123-5678','(1)12345678','(11)12345-6890',
    ]

    verifica_telefone(base_dados_telefone)

    # >>> (811)1234-5678 - não é um telefone válido.
    # >>> (21)91234-5678 - é um telefone válido.
    # >>> (14)9123-4567 - é um telefone válido.
    # >>> (11)123-5678 - não é um telefone válido.
    # >>> (1)12345678 - não é um telefone válido.
    # >>> (11)12345-6890 - é um telefone válido.