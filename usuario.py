texto = 'USUÁRIO'
print('*' * 45)
print('{:^45}'.format(texto))
print('*' * 45)

usuario = str(input("Digite seu nome: ").lower())
if(usuario == "carlos"):
    print("Seja bem vindo", usuario)
elif(usuario == "mayara"):
    print("Seja bem vinda", usuario)
elif(usuario == "neto"):
    print("Seja bem vindo", usuario)
elif(usuario == "luna"):
    print("Seja bem vinda", usuario)