quantidade = int(input())

for i in range(quantidade):
    dado = str(input())
    nomes_par_ou_impar = dado.split(' ')
    num_1, num_2 = input().split()
    num_1 = int(num_1)
    num_2 = int(num_2)
    soma = num_1 + num_2
    if(soma % 2 == 0 and nomes_par_ou_impar[1]=='PAR'):
        print(nomes_par_ou_impar[0])
    elif(soma % 2 == 1 and nomes_par_ou_impar[1]=='IMPAR'):
        print(nomes_par_ou_impar[0])
    else:
        print(nomes_par_ou_impar[2])