"""Devolvendo um valor simples
Vamos observar uma função que aceite um primeiro nome e um
sobrenome e devolva um nome completo formatado de modo elegante:"""

def nome_sobrenome(primeiro_nome, segundo_nome , terceiro_nome, quarto_nome):
    """Devolve um nome completo formatado de modo elegante."""
    nome_comleto = (f'{primeiro_nome} {segundo_nome} {terceiro_nome} {quarto_nome}')
    print('NOME COMPLETO:')
    return nome_comleto.title()

print(nome_sobrenome('carlos', 'roberto', 'conceicao', 'junior'))