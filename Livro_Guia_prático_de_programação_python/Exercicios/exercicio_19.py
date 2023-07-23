valor_total_morando = 0
def total_morangos(qtd_morangos):
    '''Cálculo do valor total dos morangos'''
    if qtd_morangos <= 5.0:
        valor_total_morando = 2.5 * qtd_morangos
    else:
        valor_total_morando = 2.2 * qtd_morangos
    return valor_total_morando

valor_total_macas = 0
def total_macas(qtd_macas):
    '''Cálculo do valor total das maçãs'''
    if qtd_macas <= 5.0:
        valor_total_macas = 1.8 * qtd_macas
    else:
        valor_total_macas = 1.5 * qtd_macas
    return valor_total_macas

'''CÁLCULO QUANTIDADE TOTAL DE FRUTAS E VALOR'''
valor_desconto = 0
def total_desconto(valor_total_frutas, qtd_total_frutas, valor_desconto):
    '''Cálculo do desconto'''
    if qtd_total_frutas > 8.0 or valor_total_frutas > 25:
        valor_desconto = valor_total_frutas * 0.1
    return valor_desconto

def total(valor_total_frutas, qtd_total_frutas, valor_desconto):
    '''Cálculo do valor final'''
    if qtd_total_frutas > 8.0 or valor_total_frutas > 25:
        valor_desconto = valor_total_frutas * 0.1
    valor_final = valor_total_frutas - valor_desconto
    return valor_final

# IMPRESSÃO DO RESULTADO
def impressao_resultados():
    print('\nResulmo da compra')
    print(f'Quantidade de Morangos: {qtd_morangos:1.2f}kg')
    print(f'Quantidade de Maçãs: {qtd_macas:1.2f}kg')
    print(f'Quantidade total de frutas: {qtd_total_frutas}kg')
    print(f'Valor dos Morangos: R${total_morangos(qtd_morangos)}')
    print(f'Valor das maçãs: R${total_macas(qtd_macas):1.2f}')
    print(f'Valor do desconto: R${total_desconto(valor_total_frutas, qtd_total_frutas, valor_desconto):1.2f}')
    print(f'Valor sem desconto: R${valor_total_frutas:1.2f}')
    print(f'Valor com desconto: R${total(valor_total_frutas, qtd_total_frutas, valor_desconto):1.2f}')

if __name__ == '__main__':
    qtd_morangos = float(input('Quantidade kg de morando: '))
    qtd_macas = float(input('Quantidade kg de maçãs: '))
    valor_total_frutas = total_morangos(qtd_morangos) + total_macas(qtd_macas)
    qtd_total_frutas = qtd_morangos + qtd_macas
    total_morangos(qtd_morangos)
    total_macas(qtd_macas)
    total_desconto(valor_total_frutas, qtd_total_frutas, valor_desconto)
    total(valor_total_frutas, qtd_total_frutas, valor_desconto)
    impressao_resultados()