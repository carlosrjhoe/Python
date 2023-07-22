numero = int(input('Digite um numero do dia (1 a 7): '))

match (numero):
    case (1):
        print('Segunda-Feira')
    case (2):
        print('Terçã-Feira')
    case (3):
        print('Quarta-Feira')
    case (4):
        print('Quinta-Feira')
    case (5):
        print('Sexta-Feira')
    case (6):
        print('Sábado')
    case (7):
        print('Domingo')
    case _:
        print('Valor inválido!')