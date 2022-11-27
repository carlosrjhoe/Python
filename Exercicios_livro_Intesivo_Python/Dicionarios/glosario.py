linguagem_de_programacao = {
    'python': 'Python é uma linguagem de programação de alto nível, interpretada de script, imperativa,         orientada a objetos, funcional, de tipagem dinâmica e forte',
    'java': 'Java é uma linguagem de programação orientada a objetos desenvolvida na década de 90 por uma equipe de programadores chefiada por James Gosling, na empresa Sun Microsystems, que em 2008 foi adquirido pela empresa Oracle Corporation.',
    'javaScript': 'JavaScript é uma linguagem de programação interpretada estruturada, de script em alto nível com tipagem dinâmica fraca e multiparadigma. Juntamente com HTML e CSS, o JavaScript é uma das três principais tecnologias da World Wide Web.',
    'go': 'Go é uma linguagem de programação criada pela Google e lançada em código livre em novembro de 2009. É uma linguagem compilada e focada em produtividade e programação concorrente, baseada em trabalhos feitos no sistema operacional chamado Inferno.',
}

for key, value in linguagem_de_programacao.items():
    """Iterar sobre um dicionário mostrando chave e valor"""
    print(f'Sobre a linguagem de programação: {key.title()}\n\t {value}\n')