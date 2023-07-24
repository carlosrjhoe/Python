def verificar_tipo_combustivel(tipo_combustivel):
    if tipo_combustivel == 'A':
        nome_tipo_combustivel = 'Álcool'
    else:
        nome_tipo_combustivel = 'Gasolina'
    return nome_tipo_combustivel

def verificar_valor_combustivel(tipo_combustivel, qnt_litros):
    if tipo_combustivel == 'A':
        valor = qnt_litros * 1.90
    else:
        valor = qnt_litros * 2.50
    return valor

valor_desconto = 0
valor_com_desconto = 0

def verificar_desconto(verificar_valor_combustivel, tipo_combustivel, qnt_litros, valor_desconto):
    if qnt_litros > 20:
        valor_desconto = verificar_valor_combustivel(tipo_combustivel, qnt_litros) * 0.05
    else:
        valor_desconto = verificar_valor_combustivel(tipo_combustivel, qnt_litros) * 0.03
    return valor_desconto

def resumo():
    print('\n\tResumo da compra\n\t')
    print(f'Tipo de combustivel: \t\t{verificar_tipo_combustivel(tipo_combustivel)}')
    print(f'Quantidade de combustivel: \t{qnt_litros}L')
    print(f'Valor total: \t\t\tR${verificar_valor_combustivel(tipo_combustivel, qnt_litros):1.2f}')
    print(f'Valor do desconto: \t\tR${verificar_desconto(verificar_valor_combustivel, tipo_combustivel,qnt_litros, valor_desconto):1.2f}')
    print(f'Valor com desconto: \t\tR${verificar_valor_combustivel(tipo_combustivel, qnt_litros) - verificar_desconto(verificar_valor_combustivel, tipo_combustivel,qnt_litros, valor_desconto):1.2f}')

if __name__ == '__main__':
    
    tipo_combustivel = input('TIPO DO COMBUSTÍVEL:\n[ A ] - Álcool\n[ G ] - Gasolina\nQual a opção? ').upper()
    qnt_litros = float(input('Quantidade de litros? '))

    verificar_tipo_combustivel(tipo_combustivel)
    verificar_valor_combustivel(tipo_combustivel, qnt_litros)
    resumo()

    # TIPO DO COMBUSTÍVEL:
    # [ A ] - Álcool
    # [ G ] - Gasolina
    # Qual a opção? a
    # Quantidade de litros? 20
    # 
            # Resumo da compra
    # 
    # Tipo de combustivel:            Álcool
    # Quantidade de combustivel:      20.0L
    # Valor total:                    R$38.00
    # Valor do desconto:              R$1.90
    # Valor com desconto:             R$36.10