"""Exercício 6.7 Faça um programa que leia uma expressão com parênteses. Usando
pilhas, verifique se os parênteses foram abertos e fechados na ordem correta.
Exemplo:"""

expressao = input('Digite a sequência de parenteses a validar: ')
x = 0
pilha = []
while x < len(expressao):
    if expressao[x] == '(':
        pilha.append('(')
    if expressao[x] == ')':
        if len(pilha) > 0:
            topo == pilha.pop(-1)
        else:
            pilha.append(')')
            break
    x =  x + 1
if len(pilha) == 0:
    print('Ok')
else:
    print('Erro')