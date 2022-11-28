while True:
    idade = int(input('Digite a sua idade para saber o valor do ingrço. Ou [sair] para encerrar a compra: '))
    
    if idade <= 3:
        print('Ingreço de graça!')
    elif idade < 12:
        print('Ingreço custa R$10,00 reais.')
    else:
        print('Ingreço custa R$15,00 reais.')
        