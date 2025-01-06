def get_horas_minutos_segundos(valor):
    horas = valor // 3600
    resto_horas = valor % 3600
    minutos = resto_horas // 60
    segundos = resto_horas % 60
    return horas, minutos, segundos


def main():
    valor = int(input())
    horas, minutos, segundos = get_horas_minutos_segundos(valor)
    print(f'{horas}:{minutos}:{segundos}')


if __name__ == '__main__':
    main()
