codigo_1, num_pec_1, valor_1 = input().split()
codigo_1, num_pec_1, valor_1 = int(codigo_1), int(num_pec_1), float(valor_1)
codigo_2, num_pec_2, valor_2 = input().split()
codigo_2, num_pec_2, valor_2 = int(codigo_2), int(num_pec_2), float(valor_2)
total_1 = num_pec_1 * valor_1
total_2 = num_pec_2 * valor_2
sub_total = total_1 + total_2

print(f'VALOR A PAGAR: R$ {sub_total:.2f}')
