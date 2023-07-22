'''
    Um funcionário ganha R$ 1.000/mês e trabalha 160 horas/mês. Quanto esse funcionário ganha por hora trabalhada?
'''

valor_hora = lambda salario, hora: salario / hora
print(f'Valor da hora trabalhada: R${valor_hora(1000,160):.2f}')