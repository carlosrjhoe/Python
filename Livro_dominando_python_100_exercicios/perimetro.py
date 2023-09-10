from math import pi

def calculates_perimeter(radius):
    perimeter = 2 * pi * radius
    return f'{perimeter:1.3f}'

def displays_result():
    print(f'The perimeter of the circle is: {calculates_perimeter(radius)}')
    
if __name__ == "__main__":
    radius = float(input('Type the radius of the circle: '))
    displays_result()