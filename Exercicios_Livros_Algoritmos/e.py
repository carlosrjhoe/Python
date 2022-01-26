prestacao = float(150.00)


class taxa():
    def taxa1(prestacao):
        return prestacao * 0.10 + (prestacao)

    def taxa2(prestacao):
        return prestacao * 0.15 + prestacao

    def taxa3(prestacao):
        return prestacao * 0.20 + prestacao


diasEmAtrazo = int(input('Quantos dias a fata esta em atrazo? '))

if diasEmAtrazo >= 0 and diasEmAtrazo <= 10:
    print(
        f'{diasEmAtrazo} dias em atrazo, juros de R${taxa.taxa1(prestacao) - prestacao}, total a pagar = R${taxa.taxa1(prestacao)}')
elif (diasEmAtrazo > 10 and diasEmAtrazo <= 15):
    print(f'{taxa.taxa2(prestacao)} dias em atrazo...')
else:
    print(f'{taxa.taxa3(prestacao)}')
