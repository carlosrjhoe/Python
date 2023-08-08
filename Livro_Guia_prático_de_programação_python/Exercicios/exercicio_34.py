def calcular_valor_final(valor_conta, dias):
    if dias <= 0:
        return valor_conta
    valor_multa = valor_conta * 0.03
    valor_juros = (0.001 * dias) * valor_conta
    valor_final = valor_conta + valor_multa + valor_juros
    return valor_final


if __name__ == "__main__":
    valor_conta = float(input('Digite o valor da conta: '))
    dias = int(input('Dias atrasados: '))
    print(f'Valor total da conta:R${calcular_valor_final(valor_conta, dias):1.2f}')
