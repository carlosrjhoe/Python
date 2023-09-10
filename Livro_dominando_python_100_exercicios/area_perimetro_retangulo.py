def calculate_perimeter_rectangle(width, length):
    perimeter = 2 * (width + length)
    return perimeter

def calculate_area_rectangle(width, length):
    area = width * length
    return area

def displays_result():
    print(f'The perimeter of the rectangle: {calculate_perimeter_rectangle(width, length):.2f}m')
    print(f'The area of the rectangle {calculate_area_rectangle(width, length):.3f}m')
    
if __name__ == "__main__":
    width = int(input('Enter the width of the rectangle: '))
    length = int(input('Enter the length of the rectangle: '))
    displays_result()