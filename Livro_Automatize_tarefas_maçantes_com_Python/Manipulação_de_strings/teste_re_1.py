import re

def procurarHeroi(heroi):
    heroiregex = re.compile(r"Batman|Tina Fey")
    mo = heroiregex.search(heroi)
    print(f'Heroi encontrado: {mo.group()}')

if __name__ == '__main__':
    procurarHeroi("Batman and Tina Fey.")