registro_compra = {}

def verificar_carne():
    tipo_carme = input('TIPO DA CARNE: [F]-Filé, [A]-Alcatra, [P]-Picanha? ').upper()
    match (tipo_carme):
        case ('F'):
            registro_compra['tipo_carne'] = 'Filé'
        case ('A'):
            registro_compra['tipo_carne'] = 'Alcatra'
        case ('P'):
            registro_compra['tipo_carne'] = 'Picanha'
    return registro_compra

def verificar_quantidade():
    registro_compra['quantidade'] = float(input('Quantidade [kg]: '))
    return registro_compra

def verificar_pagamento():
    pagamento = input('FORMA DE PAGAMENTO [C]-Cartão, [D]-Dinheiro? ').upper()
    if pagamento == 'C':
        registro_compra['forma_pagamento'] = 'Cartão'
    else:
        registro_compra['forma_pagamento'] = 'Dinheiro'
    return registro_compra

valor = 0
def verificar_valor_produto():
    qtd_minima = 5
    match (registro_compra['tipo_carne']):
        case ('Filé'):
            if registro_compra['quantidade'] > qtd_minima:
                valor = registro_compra['quantidade'] * 4.90
            else:
                valor = registro_compra['quantidade'] * 5.80
        case ('Alcatra'):
            if registro_compra['quantidade'] > qtd_minima:
                valor = registro_compra['quantidade'] * 5.90
            else:
                valor = registro_compra['quantidade'] * 6.80
        case ('Picanha'):
            if registro_compra['quantidade'] > qtd_minima:
                valor = registro_compra['quantidade'] * 6.90
            else:
                valor = registro_compra['quantidade'] * 7.80
    return valor

valor_desconto = 0
def verificar_desconto():
    if registro_compra['forma_pagamento'] == 'Cartão':
        valor_desconto = verificar_valor_produto() * 0.05
    else:
        valor_desconto = verificar_valor_produto() * 0.25
    return valor_desconto

def resumo():
    print('\n\tResumo da compra\n\t')
    print(f'Forma de pagamento: \t{registro_compra["forma_pagamento"]}')
    print(f'Tipo de carne: \t\t{registro_compra["tipo_carne"]}')
    print(f'Quantidade: \t\t{registro_compra["quantidade"]:1.3f}Kg')
    print(f'Total: \t\t\tR${verificar_valor_produto():1.2f}')
    print(f'Desconto: \t\tR${verificar_desconto():1.2f}')
    print(f'Total com desconto: \tR${verificar_valor_produto()-verificar_desconto():1.2f}')

    
if __name__ == '__main__':
    verificar_carne()
    verificar_quantidade()
    verificar_pagamento()
    verificar_valor_produto()
    verificar_desconto()
    resumo()

# TIPO DA CARNE: [F]-Filé, [A]-Alcatra, [P]-Picanha? p
# Quantidade [kg]: 8
# FORMA DE PAGAMENTO [C]-Cartão, [D]-Dinheiro? c
# 
        # Resumo da compra
# 
# Forma de pagamento:     Cartão
# Tipo de carne:          Picanha
# Quantidade:             8.000Kg
# Total:                  R$55.20
# Desconto:               R$2.76
# Total com desconto:     R$52.44