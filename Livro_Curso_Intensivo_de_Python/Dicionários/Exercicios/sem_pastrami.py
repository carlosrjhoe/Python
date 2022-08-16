"""7.9 – Sem pastrami: Usando a lista sandwich_orders do Exercício 7.8, garanta
que o sanduíche de 'pastrami' apareça na lista pelo menos três vezes.
Acrescente um código próximo ao início de seu programa para exibir uma
mensagem informando que a lanchonete está sem pastrami e, então, use um laço
while para remover todas as ocorrências de 'pastrami' e sandwich_orders.
Garanta que nenhum sanduíche de pastrami acabe em finished_sandwiches."""

from time import sleep

texto = 'LANCHONETE DE NETO E LUNA'
print('#'*len(texto))
print(f'{texto.center(len(texto))}')
print('#'*len(texto))

sanduiches = ['pastrami','misto quente', 'x-tudo', 'pastrami', 'x-burguer', 'x-salada','x-bacon','x-egg','x-frango', 'pastrami']
sanduiche_terminados = []

while sanduiches:
    sanduiche = sanduiches.pop()
    print(f'Preparando sanduiche de {sanduiche}')
    sanduiche_terminados.append(sanduiche)
    sleep(1)

texto2 = 'LISTA DE PEDIDOS PRONTOS'
print('#'*len(texto2))
print(f'{texto2.center(len(texto2))}')
for chave, pedidos in enumerate(sanduiche_terminados, start=1):
    print(f'O pedido {chave}: sanduiche de {pedidos}, está pronto!')
    sleep(1)