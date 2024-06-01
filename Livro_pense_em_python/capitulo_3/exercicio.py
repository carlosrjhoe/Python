"""Escreva uma função chamada right_justify, que receba uma string chamada s como
parâmetro e exiba a string com espaços suficientes à frente para que a última letra da
string esteja na coluna 70 da tela:"""

# def justificar_para_direita(texto):
#     print(f'{" "*70}{texto}')


"""Escreva uma função que desenhe uma grade como a seguinte:
+ - - - - + - - - - +
|         |         |
|         |         |
|         |         |
+ - - - - + - - - - +
|         |         |
|         |         |
|         |         |
+ - - - - + - - - - +
Dica: para exibir mais de um valor em uma linha, podemos usar uma sequência de
valores separados por vírgula:
print('+', '-')
Por padrão, print avança para a linha seguinte, mas podemos ignorar esse
comportamento e inserir um espaço no fim, desta forma: python print('+', end='
') print('-') A saída dessas instruções é + -. Uma instrução print sem argumento
termina a linha atual e vai para a próxima linha"""

def imprime_horizontal():
    print('+ ', ' - '*3, ' + ', ' - '*3, ' + ', sep='')

def imprime_vertical():
    print('|', ' '*11, '|', ' '*11, '|', ' '*11, sep='')

def desenhar_quadro():
    imprime_horizontal()
    for _ in range(4):
        imprime_vertical()
    imprime_horizontal()
    for _ in range(4):
        imprime_vertical()
    imprime_horizontal()

    
if __name__ == '__main__':
    desenhar_quadro()