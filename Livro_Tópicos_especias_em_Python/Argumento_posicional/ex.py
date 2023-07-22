def msg(nome, idade,/):
    """Aqui ocorre que pelo marcador “ / “ posicionado em algum ponto no campo de parâmetros de uma função, todos parâmetros situados à esquerda do mesmo serão obrigatoriamente posicionais, deixando para os demais parâmetros (à sua direita) que tenham qualquer comportamento."""
    return f'Olá {nome.title()}, você tem {idade} anos.'

def msg_1(*,nome, idade):
    """Fazendo o uso do marcador “ * “ em uma certa posição do campo de parâmetros da função, definimos que todos parâmetros que estiverem à direita deste marcador obrigatoriamente terão de ser parâmetros nomeados."""
    return f'Olá {nome.title()}, você tem {idade} anos.'

def msg_2(nome,/, idade, *, altura):
    """Pela notação, o primeiro parâmetro (nome) é obrigatoriamente posicional/justaposto, o segundo parâmetro (idade) é justaposto apenas pela posição que o mesmo se encontra, por fim o terceiro parâmetro (altura) é obrigatoriamente nomeado."""
    return f'Olá {nome.title()}, você tem {idade} anos e mede {altura}m.'

if __name__ == '__main__':
    print(msg('carlos', 37))
    print(msg_1(nome ='mayara', idade =38))
    print(msg_2('neto', 7, altura=1.10))
    print(msg('luna', 5))