"""Exercício 5.14 Escreva um programa que leia números inteiros do teclado. O programa deve ler os números até que o usuário digite 0 (zero). No final da execução,
exiba a quantidade de números digitados, assim como a soma e a média aritmética."""

soma = 0
while True:
    num = int(input('Digite um numero para somar, ou "0" para sair: '))
    if num == 0:
        break
    else:
        soma = soma + num
print(soma)
