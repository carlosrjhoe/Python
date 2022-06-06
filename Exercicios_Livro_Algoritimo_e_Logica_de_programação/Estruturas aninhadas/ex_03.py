""" Exercício 4.9 Escreva um programa para aprovar o empréstimo bancário para
compra de uma casa. O programa deve perguntar o valor da casa a comprar, o
salário e a quantidade de anos a pagar. O valor da prestação mensal não pode ser
superior a 30% do salário. Calcule o valor da prestação como sendo o valor da
casa a comprar dividido pelo número de meses a pagar """

valor = float(input('Qual o valor ca casa que deseja comprar? '))
salario = float(input('Qual o seu salário? '))
anos = int(input('Em quantos anos deseja pagar o emprestimo? '))
meses = anos * 12

trinta_porcento_salario = salario * 0.3
parcela = (valor / meses)

if parcela > trinta_porcento_salario:
    print('Parcela superior a 30% do seu salário.')
else:
    print(f'A sua parcela será de R${parcela:.2f}')


""" Exercício 4.9 Escreva um programa para aprovar o empréstimo bancário para
compra de uma casa. O programa deve perguntar o valor da casa a comprar, o
salário e a quantidade de anos a pagar. O valor da prestação mensal não pode ser
superior a 30% do salário. Calcule o valor da prestação como sendo o valor da
casa a comprar dividido pelo número de meses a pagar """

valor = float(input('Qual o valor ca casa que deseja comprar? '))
salario = float(input('Qual o seu salário? '))
anos = int(input('Em quantos anos deseja pagar o emprestimo? '))
meses = anos * 12

trinta_porcento_salario = salario * 0.3
parcela = (valor / meses)

if parcela > trinta_porcento_salario:
    print('Parcela superior a 30% do seu salário.')
else:
    print(f'A sua parcela será de R${parcela:.2f}')
