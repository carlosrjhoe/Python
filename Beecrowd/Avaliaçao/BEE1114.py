SENHA = 2002
log_senha = int(input())
while log_senha != SENHA:
    print('Senha Invalida')
    log_senha = int(input())
    if log_senha == SENHA:
        print('Acesso Permitido')
        break