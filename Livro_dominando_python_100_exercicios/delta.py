def get_coefficients():
    for i in range(1, 4):
        i = int(input(f'Enter the {i} coefficient: '))
        coefficients.append(i)

def calculate_delta():
    a, b, c = coefficients
    delta = b**2 - 4*a*c
    return delta

def displays_result():
    print(f'The delta of the second degree equation is {calculate_delta()}')
        
if __name__ == "__main__":
    coefficients = []
    get_coefficients()
    displays_result()