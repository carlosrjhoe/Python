frase = 'Diga-me uma coisa, e eu vou repetir de volta para você:'
# ativo = True
msg = ''

while True:
    print(frase)
    msg = input("Digite 'sair' para encerrar o programa. ")
    if msg == 'sair':
        break
    else:
        print(msg)
