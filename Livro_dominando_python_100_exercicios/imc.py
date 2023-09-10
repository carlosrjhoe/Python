def get_imc(weight, height):
    imc = weight / (height**2)
    return f'{imc:.2f}'

if __name__ == "__main__":
    weight = float(input('Digite seu peso em (kg): '))
    height = float(input('Digite sua altura em (m): '))
    print(f'Seu índice de massa corporal (IMC): {get_imc(weight, height)}')