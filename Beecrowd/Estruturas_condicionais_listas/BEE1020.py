def get_idade_dias_em_meses_anos(valor):
    anos = valor // 365
    resto_anos = int(valor % 365)
    meses = int(resto_anos // 30)
    dias = int(resto_anos % 30)
    return anos, meses, dias


def main():
    valor = int(input())
    ano, meses, dias = get_idade_dias_em_meses_anos(valor)
    print(f'{ano} ano(s)')
    print(f'{meses} mes(es)')
    print(f'{dias} dia(s)')


if __name__ == '__main__':
    main()
