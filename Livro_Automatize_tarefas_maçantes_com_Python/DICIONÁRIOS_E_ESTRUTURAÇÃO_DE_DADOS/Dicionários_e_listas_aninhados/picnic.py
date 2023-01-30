todos_convidados = {
    'carlos': {'maçâ': 3, 'pera': 4},
    'mayara': {'ameixa': 2, 'pinha': 2},
    'neto': {'nutela': 1, 'pão': 3},
    'luna': {'tomate': 3, 'biscoito': 4},
}

def totalTrazido(todos_convidados, item):
    numTrazido = 0
    for i, j in todos_convidados.items():
        numTrazido = numTrazido + j.get(item, 0)
    return numTrazido

def apresentacao(totalTrazido, todos_convidados):
    print("Número de coisas que estão sendo trazidas:")
    print(f'- Maçâ: {str(totalTrazido(todos_convidados, "maçâ"))}')
    print(f'- Pera: {str(totalTrazido(todos_convidados, "pera"))}')
    print(f'- Ameixa: {str(totalTrazido(todos_convidados, "ameixa"))}')
    print(f'- Tomate: {str(totalTrazido(todos_convidados, "tomate"))}')
    print(f'- Pinha: {str(totalTrazido(todos_convidados, "pinha"))}')
    print(f'- Nutela: {str(totalTrazido(todos_convidados, "nutela"))}')
    print(f'- Pão: {str(totalTrazido(todos_convidados, "pão"))}')


if __name__ == '__main__':
    apresentacao(totalTrazido, todos_convidados)