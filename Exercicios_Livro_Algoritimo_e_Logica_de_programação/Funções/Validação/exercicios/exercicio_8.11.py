"""Exercício 8.11 Escreva uma função para validar uma variável string. Essa função
recebe como parâmetro a string, o número mínimo e máximo de caracteres. Retorne
verdadeiro se o tamanho da string estiver entre os valores de máximo e mínimo,
e falso em caso contrário"""

def validacao(s, minimo, maximo):
    tamanho = len(s)
    return minimo <= tamanho <= maximo

print(validacao("",1,5))
print(validacao("ABC",2,5))
print(validacao("ABCDEFG",1,10))