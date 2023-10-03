def imc(peso, altura):
    imc = peso / (altura**2)
    return imc

def categoria_imc(peso, altura):
    if imc(peso, altura) < 18.5:
        categoria = 'Abaixo do peso'
    elif imc(peso, altura) < 25:
        categoria = 'Peso normal'
    elif imc(peso, altura) < 30:
        categoria = 'Sobrepeso'
    elif imc(peso, altura) < 35:
        categoria = 'Obesidade'
    else:
        categoria = 'Obesidade grave'
    return categoria

if __name__ == "__main__":
    peso = float(input('Digite seu peso em (kg): '))
    altura = float(input('Digite sua altura em (m): '))
    print(f'Seu IMC é de: {imc(peso, altura):1.2f}')
    print(f'{categoria_imc(peso, altura)}')
    