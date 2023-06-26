"""12 – Crie uma expressão regular que valide se uma string é um endereço de e-mail válido. Teste a expressão regular com alguns exemplos de endereços de e-mail válidos e inválidos:"""

import re

def verifica_email(base_dados_email):
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    for email in base_dados_email:
        if re.match(email_regex, email):
            """verificar se cada endereço de e-mail corresponde à expressão regular email_regex."""
            print(f'{email} - é um email válido.')
        else:
            print(f'{email} - não é um email válido.')

if __name__ == '__main__':
    base_dados_email = [
        'usuario1234gmail.com','usuario1@.com','usuario124@hotmail.com',
        'usuario234@gmail.','usuario@gmail.com','usuario4.sobre@.com'
    ]
    
    verifica_email(base_dados_email)

    # >>> usuario1234gmail.com - não é um email válido.
    # >>> usuario1@.com - não é um email válido.
    # >>> usuario124@hotmail.com - é um email válido.
    # >>> usuario234@gmail. - não é um email válido.
    # >>> usuario@gmail.com - é um email válido.
    # >>> usuario4.sobre@.com - não é um email válido.