"""Exercício 3.4 Escreva uma expressão para determinar se uma pessoa deve ou não
pagar imposto. Considere que pagam imposto pessoas cujo salário é maior que
R$ 1.200,00."""

SALARIO_MINIMO = 1200
salario = float(input())

if salario <= SALARIO_MINIMO:
    print('Não vai pagar IMPOSTO')
else:
    print('Vai pagar IMPOSTO')