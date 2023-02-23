def inicio():
    print('Dê-me dois números e eu os dividirei.')
    print('Digite [Q] para sair.')
    return

def perguntas():
    while True:
        primeiro_numero = input('Primeiro número: ').upper()
        if primeiro_numero == 'Q':
            print('Sair...')
            break
        segundo_numero = input('Segundo número: ').upper()
        if segundo_numero == 'Q':
            print('Sair...')
            break
        try:
            resposta = int(primeiro_numero) / int(segundo_numero)
            print(f'Resultado: {resposta}')
        except ZeroDivisionError:
            print('Você não pode dividir por zero')

if __name__ == '__main__':
    inicio()
    perguntas()