"""7.8 – Lanchonete: Crie uma lista chamada sandwich_orders e a preencha com os
nomes de vários sanduíches. Em seguida, crie uma lista vazia chamada
finished_sandwiches. Percorra a lista de pedidos de sanduíches com um laço e
mostre uma mensagem para cada pedido, por exemplo, Preparei seu sanduíche
de atum. À medida que cada sanduíche for preparado, transfira-o para a lista de
sanduíches prontos. Depois que todos os sanduíches estiverem prontos, mostre uma
mensagem que liste cada sanduíche preparado"""

from time import sleep

texto = 'LANCHONETE DE NETO E LUNA'
print('#'*len(texto))
print(f'{texto.center(len(texto))}')
print('#'*len(texto))

sanduiches = ['misto quente', 'x-tudo', 'x-burguer', 'x-salada','x-bacon','x-egg','x-frango']
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

    