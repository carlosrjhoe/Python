def conversor_int_para_str(numero):
    match numero:
        case 0: return 'Zero'
        case 1: return 'Um'
        case 2: return 'Dois'
        case 3: return 'Tres'
        case 4: return 'Quatro'
        case 5: return 'Cinco'
        case 6: return 'Seis'
        case 7: return 'sete'
        case 8: return 'Oito'
        case 9: return 'Nove'
        case 10: return 'Dez'

if __name__ == '__main__':
    numero = int(input('Digite um número de [0 a 10]: '))
    print(conversor_int_para_str(numero))