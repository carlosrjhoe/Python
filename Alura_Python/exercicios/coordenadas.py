def coordenadas():
    x = int(input('Digite 1° coordenada: '))
    y = int(input('Digite 2° coordenada: '))
    
    if x > 0 and y > 0:
        print('Primeiro Quadrante.')
    elif x < 0 and y < 0:
        print('Terceiro Quadrante.')
    elif x < 0 and y > 0:
        print('Segundo Quadrante.')
    elif x > 0 and y < 0:
        print('Quarto Quadrante.')
    else:
        print('Ponto está localizado no eixo ou origem.')
        

def main():
    coordenadas()

if __name__ == "__main__":
    main()