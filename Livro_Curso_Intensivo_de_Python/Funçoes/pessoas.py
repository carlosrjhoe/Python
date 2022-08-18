def imprime_moledos(desenhos_nao_impressos, modelos_completados):
    while desenhos_nao_impressos:
        design_atual = desenhos_nao_impressos.pop()
        print(f'Modelo de impressao: {design_atual}')
        modelos_completados.append(design_atual)
        

def mostrar_modelos_concluídos(modelos_completados):
    print(f'Os seguintes modelos foram impressos:')
    for modelos in modelos_completados:
        print(f'{modelos}')


desenhos_nao_impressos = ['iphone case', 'robot pendant', 'dodecahedron']
modelos_completados = []

imprime_moledos(desenhos_nao_impressos[:], modelos_completados)
mostrar_modelos_concluídos(modelos_completados)
