'''
    Alguns amigos foram a um restaurante e decidiram dividir a conta em partes iguais. Quanto ficou a parte de cada um?
    Quantidade de pessoas? 5 
    Valor da conta? 100
 '''

valor_conta = lambda qtda_pessoas, valor_conta: valor_conta / qtda_pessoas
print(f'Divisão da conta: R${valor_conta(5, 100):.2f} para cada pessoa.')