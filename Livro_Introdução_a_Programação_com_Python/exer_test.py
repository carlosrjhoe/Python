# salario = float(input('Digite o salário para cálculo do imposto de renda: '))
# base = salario
# imposto = 0

# if base > 3000:
#     imposto = imposto + ((base - 3000) * 0.35)
#     base = 3000
# if base > 1000:
#     imposto = imposto + ((base - 1000) * 0.20)
# print(f'Sálario R${salario:.2f} Imposto a pagar R$ {imposto:.2f}')

# x = 0
# while x <= 3:
#     print(x)
#     x += 1

# """ Listagem 5.7 – Impressão de números pares de 0 até um número digitado pelo usuário"""

# fim = int(input(''))
# x = 0
# while x <= fim:
#     print(x)
#     x += 1

"""Listagem 5.10 – Contagem de questões corretas"""

pontos = 0
questao = 1
while questao <= 3:
    resposta = input(f'Resposta da questão {questao}: ').upper()
    if questao == 1 and resposta == 'B':
        pontos += 1
    if questao == 2 and resposta == 'A':
        pontos += 1
    if questao == 3 and resposta == 'C':
        pontos += 1
    questao += 1
print(f'O aluno fez {pontos} pontos.')