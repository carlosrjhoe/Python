# x = y = 1
# print(x, y)

"""O volume de uma esfera com raio r é . Qual é o volume de uma esfera com raio 5?"""
# raio = 5

# volume = (4 / 3) * 3.14 * (raio ** 3)
# print(f'O volume de uma esfera com {raio} de raio terá {volume:.3f} metros cúbicos')

"""Suponha que o preço de capa de um livro seja R$ 24,95, mas as livrarias recebem um
desconto de 40%. O transporte custa R$ 3,00 para o primeiro exemplar e 75 centavos
para cada exemplar adicional. Qual é o custo total de atacado para 60 cópias?"""
copias, preco_capa, desconto, custo_transporte, custo_transporte_adicional = 60, 24.95, 0.40, 3.00, 0.75

# Calcular preco com  desconto
preco_desconto = preco_capa * (1 - desconto)

# Custo custo total dos livros
custo_total_livros = preco_desconto * copias

# Custo total do transporte
custo_total_tranporte = custo_transporte + (custo_transporte_adicional * (copias - 1))

# Calcular custo total
custo_total = custo_total_livros + custo_total_tranporte

print(f'O custo total de atacado para {copias} cópias é R$ {custo_total:.2f}')