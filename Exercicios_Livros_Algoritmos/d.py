def distancia_percorrida():
    return tempo * velovidade

def litros_gasto_de_gasolina(distancia_percorrida):
    return distancia_percorrida() / 12

tempo = int(input('Tempo de viagem: '))
velovidade = int(input('Velocidade média em (km/h): '))

print(f'A distancia percorrida foi de {distancia_percorrida()}km')
print(f'E gastou certa de {litros_gasto_de_gasolina(distancia_percorrida)}Lts de gasolina')

