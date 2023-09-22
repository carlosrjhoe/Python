def calcula_perimetro_do_triagulo():
    perimetro = lado_a + lado_b + lado_c
    return perimetro

def calcular_area_do_triagulo():
    area = (lado_b * altura_lado_b) / 2
    return area

if __name__ == "__main__":
    lado_a = float(input('Digite o lado A do triangulo: '))
    lado_b = float(input('Digite o lado B do triangulo: '))
    lado_c = float(input('Digite o lado C do triangulo: '))
    altura_lado_b = float(input('Digite a altura relativa ao lado B do triangulo: '))
    print(f'O perimetro do triângulo é: {calcula_perimetro_do_triagulo()}')
    print(f'A área do triângulo é: {calcular_area_do_triagulo()}')
    

    