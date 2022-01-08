def ceulcius(x):
    return (x - 32)/1.8
    
x = int(input('Digite uma temperatura em (F°): '))
print(f'A temperatura digitada em {x}F°, é igual a {ceulcius(x):.1f}C°')