""" Listagem 6.22 – Pilha de pratos"""
prato = 5
pilha = list(range(1,prato+1))
while True:
    print(f'Exitem {len(pilha)} pratos na pilha.\nPilha atual {pilha}.\nDigite [E] para empilhar um novo prato,\nOu [D] para desempilhar.\n[S] para sair.')
    operacao = input('Operação [E, D ou S]: ').upper()
    if operacao == 'D':
        if (len(pilha)) > 0:
            lavado = pilha.pop(-1)
            print(f'Prato {lavado} lavado.')
        else:
            print('Pilha vazia! Nada para lavar...')
    elif operacao == 'E':
        prato += 1
        pilha.append(prato)
    elif operacao == 'S':
        break
    else:
        print('Operação invalida! Digite apenas E, D ou S.')