def calcular_velocidade_media():
    velocidade_media = delta_s / delta_t
    return velocidade_media

if __name__ == "__main__":
    delta_s = float(input('Digite a variação de espaço (DELTA_S): '))
    delta_t = float(input('Digite a variação de tempo (DELTA_T): '))

    print(f'A velocidade média é: {calcular_velocidade_media()}')