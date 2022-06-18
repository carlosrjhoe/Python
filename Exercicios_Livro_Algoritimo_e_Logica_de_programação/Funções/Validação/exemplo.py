"""Listagem 8.15 – Exemplo de validação sem usar uma função"""

# while True:
#     v = int(input('Digite um valor entre [0 e 5]: '))
#     if v < 0 or v > 5:
#         print('Valor inválido...')
#     else:
#         break

"""Listagem 8.16 – Validação de inteiro usando função"""

def faixa_int(pergunta, minimo, maximo):
    while True:
        v = int(input(pergunta))
        if v < minimo or v > maximo:
            print(f'Valor inválido. Digite o valor entre {minimo} e {maximo}')
        else:
            return v
        
faixa_int('numero ', 0,100)