from random import randint


class Die:
    def __init__(self, sides=6):
        self.sides = sides
       
    def roll_die(self):
        numero = randint(1, self.sides)
        print(f"{numero}")
        return


if __name__ == '__main__':
    numero_morte = Die(10)
    numero_morte.roll_die()