clientes_academia = []
def verificar_clientes():
    while True:
        codigo = int(input('Digite seu código: '))
        if codigo == 0:
            break
        else:
            nome = input('Digite seu nome: ').title()
            altura = float(input('Digite sua altura: '))
            peso = float(input('Digite seu peso: '))

        clientes = {
            'codigo': codigo,
            'nome': nome,
            'altura': altura,
            'peso': peso
        }
        clientes_academia.append(clientes)    
    return clientes_academia

def total_alturas():
    total_alturas = 0
    for cliente in clientes_academia:
        altura = cliente['altura']
        total_alturas += altura
    return total_alturas

def total_pesos():
    total_pesos = 0
    for cliente in clientes_academia:
        peso = cliente['peso']
        total_pesos += peso
    return total_pesos

def maior_cliente():
    maior_cliente = {}
    for cliente in clientes_academia:
        altura = cliente['altura']
        if 'altura' in maior_cliente:
            if altura > maior_cliente['altura']:
                maior_cliente = cliente
        else:
            maior_cliente = cliente
    return maior_cliente['nome']

def menor_cliente():
    menor_cliente = {}
    for cliente in clientes_academia:
        altura = cliente['altura']
        if 'altura' in menor_cliente:
            if altura < menor_cliente['altura']:
                menor_cliente = cliente
        else:
            menor_cliente = cliente
    return menor_cliente['nome']

def cliente_mais_gordo():
    cliente_gordo = {}
    for cliente in clientes_academia:
        peso = cliente['peso']
        if 'peso' in cliente_gordo:
            if peso > cliente_gordo['peso']:
                cliente_gordo = cliente
        else:
            cliente_gordo = cliente
    return cliente_gordo['nome']

def cliente_mais_magro():
    cliente_magro = {}
    for cliente in clientes_academia:
        peso = cliente['peso']
        if 'peso' in cliente_magro:
            if peso < cliente_magro['peso']:
                cliente_magro = cliente
        else:
            cliente_magro = cliente
    return cliente_magro['nome']

def qtd_clientes():
    qtd = len(clientes_academia)
    return  qtd

def media_altura():
    altura = total_alturas()
    clientes = qtd_clientes()
    media = altura / clientes
    return media

def media_peso():
    media = total_pesos / qtd_clientes()
    return media

if __name__ == '__main__':
    print(verificar_clientes())
    print(f'Total de clientes: {qtd_clientes()}')
    print(f'Total altura: {total_alturas()}m')
    print(f'Total peso: {total_pesos()}Kg')
    print(f'Maior cliente: {maior_cliente()}')
    print(f'Menor cliente: {menor_cliente()}')
    print(f'Cliente mais gordo: {cliente_mais_gordo()}')
    print(f'Cliente mais magro: {cliente_mais_magro()}')
    print(f'Media de altura: {media_altura()}m')
    print(f'Media de peso: {media_peso()}Kg')