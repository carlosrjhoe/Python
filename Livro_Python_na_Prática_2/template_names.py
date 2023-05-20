"""– Crie um template de mala direta contendo uma mensagem, envie a mensagem para 5 pessoas listadas em uma simples base de dados aqui representada pela lista nomes = ['Anna', 'Paulo', 'Maria', 'Rafael', 'Patricia'] de modo que a mensagem seja personalizada a cada um dos nomes da lista.
"""

from string import Template

def mensagemPersonalizada(nomes, template):
    for i in nomes:
        print(f'{template.substitute(nome=i)}')
        print('-'*77)

if __name__ == '__main__':
    nomes = ['Anna', 'Paulo', 'Maria','Rafael','Patricia']
    email = """Olá $nome, Seja bem vindo(a) ao curso de Python!!! Abraço, Carlos Roberto"""
    template = Template(email)
    mensagemPersonalizada(nomes, template)
    