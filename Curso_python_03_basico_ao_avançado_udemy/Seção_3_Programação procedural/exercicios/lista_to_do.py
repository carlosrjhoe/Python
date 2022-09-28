"""
    Faça uma lista de tarefas com as seguintes opções:
        1° Adicionar tarefa
        2° Listar tarefas
        3° Opção de desfazer (a cada que chamarmos, desfazer a última opção)
        4° Opção de refazer (a cada que chamarmos, refazer a última opção)
    
"""

def cabecalho():
    texto = 'Exercicio de Python (Todo Lista)'
    print(f'{"#"*len(texto)*2}')
    print(f'{texto.center(len(texto)*2)}')
    print(f'{"#"*len(texto)*2}\n')
    return

def opcao():
    lista_desfazer = []
    lista_refazer = []
    
    while True:
        cabecalho()
        todo = input('Digite uma tarefa ou [apagar, refazer, listar]: ').upper()        
        if todo == 'LISTAR':
            if len(lista_desfazer) == 0:
                print('Sem tarefas')
            else:
                mostrar_opcoes(lista_desfazer)
            continue
        elif todo == 'APAGAR':
            apagar(lista_desfazer, lista_refazer)
            continue
        elif todo == 'REFAZER':
            refazer(lista_desfazer, lista_refazer)
            continue
        
        adcionar(todo, lista_desfazer)

def mostrar_opcoes(lista_desfazer):
    texto = 'LISTA DE TAREFAS'
    print(f'\n{"#"*len(texto)*4}')
    print(f'{texto.center(len(texto)*4)}')
    print(f'{"#"*len(texto)*4}')
    print(f'\n{lista_desfazer}\n')

def apagar(lista_desfazer, lista_refazer):
    if not lista_desfazer:
        print('Nada para apagar.\n')
        return
    
    ultima_tarefa = lista_desfazer.pop()
    lista_refazer.append(ultima_tarefa)
    print(f'Apagando... {ultima_tarefa}\n')

def refazer(lista_desfazer, lista_refazer):
    if not lista_refazer:
        print('Nada para refazer.\n')
        return
    
    ultima_tarefa = lista_refazer.pop()
    lista_desfazer.append(ultima_tarefa)
    print(f'Refazendo... {ultima_tarefa}\n')

def adcionar(todo, lista_desfazer):
    lista_desfazer.append(todo)

if __name__ == '__main__':
    opcao()