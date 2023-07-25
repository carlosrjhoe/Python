inf_inss = {}

def salario_bruto():
    inf_inss['hora_trabalhada'] = int(input(f'Quantas horas foram trabalhadas? '))
    inf_inss['valor_hora'] = float(input(f'Qual o valor da hora trabalhada? '))
    inf_inss['salario_bruto'] = inf_inss['hora_trabalhada'] * inf_inss['valor_hora']
    return inf_inss['salario_bruto']

def desconto_sindcato():
    inf_inss['sidicato'] = inf_inss['salario_bruto'] * 0.03
    return inf_inss['sidicato']

def aliquota_imposto_renda():
    if inf_inss['salario_bruto'] <= 2826.65:
        inf_inss['aliquota_IR'] = 0.075
    elif inf_inss['salario_bruto'] >= 2826.66 and inf_inss['salario_bruto'] <= 3751.05:
        inf_inss['aliquota_IR'] = 0.15
    elif inf_inss['salario_bruto'] >= 3751.06 and inf_inss['salario_bruto'] <= 4663.68:
        inf_inss['aliquota_IR'] = 0.225
    elif inf_inss['salario_bruto'] >= 4664.68:
        inf_inss['aliquota_IR'] = 0.275
    return inf_inss['aliquota_IR']

def desconto_impost_renda():
    inf_inss['desc_imposto_renda'] = inf_inss['salario_bruto'] * inf_inss['aliquota_IR']
    return inf_inss['desc_imposto_renda']

def aliquota_inss():
    if inf_inss['salario_bruto'] <= 1751.81:
        inf_inss['aliquota_inss'] = 0.08
    elif inf_inss['salario_bruto'] >= 1751.82 and inf_inss['salario_bruto'] <= 2919.72:
        inf_inss['aliquota_inss'] = 0.09
    elif inf_inss['salario_bruto'] >= 2919.73:
        inf_inss['aliquota_inss'] = 0.11
    return inf_inss['aliquota_inss']

def desconto_inss():
    if inf_inss['salario_bruto'] <= 5839.45:
        inf_inss['desc_inss'] = inf_inss['salario_bruto'] * inf_inss['aliquota_inss']
    else:
        inf_inss['desc_inss'] = 5839.45 * inf_inss['aliquota_IR']
    return inf_inss['desc_inss']

def salario_liquido():
    inf_inss['salario_liquido'] = inf_inss['salario_bruto'] - inf_inss['sidicato'] - inf_inss['desc_inss']
    return inf_inss['salario_liquido'] 

def total_desconto():
    inf_inss['total_desconto'] = inf_inss['sidicato'] + inf_inss['desc_imposto_renda'] + inf_inss['desc_inss']
    return inf_inss['total_desconto']

def atualizar_salario():
    inf_inss['salario_com_desconto'] = inf_inss['salario_bruto'] - inf_inss['total_desconto']
    return inf_inss['total_desconto']
    
def resumo():
    print('\n\tResumo do contra-cheque\n\t')
    for chave, valor in inf_inss.items():
        print(f'{chave}\tR${valor:1.2f}')
    

if __name__ == '__main__':
    salario_bruto()
    desconto_sindcato()
    aliquota_imposto_renda()
    desconto_impost_renda()
    aliquota_inss()
    desconto_inss()
    total_desconto()
    atualizar_salario()
    resumo()

    # Quantas horas foram trabalhadas? 220
    # Qual o valor da hora trabalhada? 7.5
    # 
            # Resumo do contra-cheque
    # 
    # hora_trabalhada R$220.00
    # valor_hora      R$7.50
    # salario_bruto   R$1650.00
    # sidicato        R$49.50
    # aliquota_IR     R$0.07
    # desc_imposto_renda      R$123.75
    # aliquota_inss   R$0.08
    # desc_inss       R$132.00
    # total_desconto  R$305.25
    # salario_liquido R$1468.50