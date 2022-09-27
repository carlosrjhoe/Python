"""
    Faça uma lista de tarefas com as seguintes opções:
        1° Adicionar tarefa
        2° Listar tarefas
        3° Opção de desfazer (a cada que chamarmos, desfazer a última opção)
        4° Opção de refazer (a cada que chamarmos, refazer a última opção)
    
"""


def mostrar_opcoes(lista_desfazer):
    texto = 'LISTA DE TAREFAS'
    print(f'{"#"*len(texto)*3}')
    print(f'{texto.center(len(texto)*3)}')
    print(f'{"#"*len(texto)*3}')
    print(lista_desfazer)


def apagar(lista_desfazer, lista_refazer):
    if not lista_desfazer:
        print('Nada a desfazer')
        return
    
    last_todo = lista_desfazer.pop()
    lista_refazer.append(last_todo)

def refazer(lista_desfazer, lista_refazer):
    if not lista_refazer:
        print('Nada a refazer.')
        return
    
    ultima_tarefa = lista_refazer.pop()
    lista_desfazer.append(ultima_tarefa)


def adcionar(todo, lista_desfazer):
    lista_desfazer.append(todo)


if __name__ == '__main__':
    lista_desfazer = []
    lista_refazer = []
    
    while True:
        todo = input('Digite uma tarefa ou [apagar, refazer, listar]: ')
        
        if todo == 'listar':
            if len(lista_desfazer) == 0:
                print('Sem tarefas')
            else:
                mostrar_opcoes(lista_desfazer)
            continue
        elif todo == 'apagar':
            apagar(lista_desfazer, lista_refazer)
            continue
        elif todo == 'refazer':
            refazer(lista_desfazer, lista_refazer)
            continue
        
        adcionar(todo, lista_desfazer)