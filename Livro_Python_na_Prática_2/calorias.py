def perdaCaloricas(CONSTANTE):
    peso = int(input('Informe seu peso [kg]: '))
    km_h = int(input('Informe km/h percorrido: '))
    tempo_percorrido = int(input('Informe tempo percorrido em [min]: '))
    calorias_perdica = (peso * km_h * CONSTANTE) * tempo_percorrido
    print(f'Você teve uma perda de {calorias_perdica:.2f}Kcal')
    return
    
if __name__ == '__main__':
    CONSTANTE = 0.0175
    perdaCaloricas(CONSTANTE)