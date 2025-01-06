a, b, c = input().split()
a, b, c = float(a), float(b), float(c)
PI = 3.14159
area_triagulo = (a * c) / 2
area_circulo = PI * pow(c, 2)
area_trapezio = ((a + b) * c) / 2
area_quadrado = pow(b, 2)
area_retangulo = a * b
print(f'TRIANGULO: {area_triagulo:.3f}')
print(f'CIRCULO: {area_circulo:.3f}')
print(f'TRAPEZIO: {area_trapezio:.3f}')
print(f'QUADRADO: {area_quadrado:.3f}')
print(f'RETANGULO: {area_retangulo:.3f}')
