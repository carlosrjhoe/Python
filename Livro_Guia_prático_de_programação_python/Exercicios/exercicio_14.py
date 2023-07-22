credito = float(input('Digite o valor do crédito: '))
valor_do_produto = float(input('Digite o valor do produto: '))

if credito >= valor_do_produto:
    print('Compra aprovada!')
else:
    print('Não foi possivel realizar a compra.')