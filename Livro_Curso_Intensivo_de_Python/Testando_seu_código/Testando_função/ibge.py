maisNovo = 999
maisVelho = 0
qtdEntrevistados = 0
menoresIdade = 0
mediaIdades = 0.0
somaIdades = 0

while qtdEntrevistados < 5:
    idade = int(input('Qual a sua idade:'))

    if idade > maisVelho:
        maisVelho = idade
    if idade < maisNovo:
        maisNovo = idade
    if idade < 18:
        menoresIdade += 1
        
    qtdEntrevistados += 1
    somaIdades = somaIdades + idade
    mediaIdades = somaIdades / qtdEntrevistados
    

print(f'O mais novo tem {maisNovo} anos idade')
print(f'O mais velho tem {maisVelho} anos idade')
print(f'O total de intrevistados {qtdEntrevistados}')
print(f'O qtd de menores de idade {menoresIdade}.')
print(f'A média das idade {mediaIdades}.')