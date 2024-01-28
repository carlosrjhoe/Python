nome = input()
salario = float(input())
total_vendas = float(input())
comissao = total_vendas * 0.15
print(f'TOTAL = R$ {(salario + comissao):.2f}')