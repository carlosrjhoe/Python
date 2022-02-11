num = int(input('Digite um número: '))
divisoes = 0

for i in range(1, num + 1):
    if num % i == 0:
        divisoes += 1
        '''Criei um laço para percorrer de "i" em range, e se "i" o resto da divisão for igual a 0, implementa a variavel "divisao" + 1'''
if divisoes == 2:
    '''Se a variavel "divisoes" for igual a 2, a variavel "num" é primo'''
    print(f'{num} é primo')
    print(f'{num} é divisivel por 1 ou por {num}')
else:
    print(f'{num} não é primo')
    print(f'{num} é divisível {divisoes} vezes...')