def soma(x, y, z=None):
    if z is not None:
        print(f'{x}-{y}-{z}')
    else:
        print(f'{x}-{y}')

if __name__ == '__main__':
    soma(1,2,5)