from time import sleep


def mult(*args):
    total = 1
    for i in args:
        total *= i
    return total


def parOuImpar(*args):
    for i in args:
        sleep(1)
        if i % 2 == 0:
            print(f"O número {i} é PAR")
        else:
            print(f"O número {i} é IMPAR")


if __name__ == "__main__":
    print(mult(1, 2, 3, 4, 5))
    parOuImpar(1, 2, 3, 4, 5)
