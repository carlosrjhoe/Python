'''Vamos converter metros para centímetros?!
    Escreva um código que: 
        1) Solicita a quantidade de metros. 
        2) Calcula a quantidade de centímetros, com base na quantidade de metros informada. 
        3) Imprima o resultado. 
        DICAS 1)
            1 metro tem 100 centímetros, ou seja, multiplique por 100 o valor do metro. 
            2) O valor do metro deve ser convertido para float().
'''


metros = float(input('Informe a quantidade de metros: '))
metros_para_centimetro = lambda metros, centimetros=100: metros * centimetros
print(f'{metros_para_centimetro(metros)}cm')
