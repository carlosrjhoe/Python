nome = input()
salario = float(input())
total_vendas = float(input())
comissao = total_vendas * 0.15
total_receber = salario + comissao

print(f"TOTAL = R$ {total_receber:.2f}")
