tipo_combustivel = input('''TIPO DO COMBUSTÍVEL:\n[ A ] - Álcool\n[ G ] - Gasolina\nQual a opção? ''').upper()
qnt_litros = float(input('Quantidade de litros? '))

nome_tipo_combustivel = ''
valor = 0
valor_desconto = 0
valor_com_desconto = 0

if tipo_combustivel == 'A':
    nome_tipo_combustivel = 'Álcool'
    valor = qnt_litros * 4.19
    if qnt_litros > 20:
        valor_desconto = valor * 0.05
        valor_com_desconto = valor - valor_desconto
    else:
        valor_desconto = valor * 0.03
        valor_com_desconto = valor - valor_desconto
else:
    nome_tipo_combustivel = 'Gasolina'
    valor = qnt_litros * 5.59
    if qnt_litros > 20:
        valor_desconto = valor * 0.05
        valor_com_desconto = valor - valor_desconto
    else:
        valor_desconto = valor * 0.03
        valor_com_desconto = valor - valor_desconto

print('\n\tResumo da compra\n\t')
print(f'Tipo de combustivel: {nome_tipo_combustivel}')
print(f'Quantidade de combustivel(L): {qnt_litros:1.2f}L')
print(f'Valor total: R${valor:1.2f}')