def qual_sua_idade():
    idade = int(input('Qual sua idade: '))

    if idade < 12:
        print('Criança')
    elif 13 < idade < 18:
        print('Adolecente')
    elif idade >= 18:
        print('Adulto')
        
def main():
    qual_sua_idade()

if __name__ == "__main__":
    main()        