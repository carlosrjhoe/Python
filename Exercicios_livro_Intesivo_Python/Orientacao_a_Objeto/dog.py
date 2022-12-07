class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age


    def sit(self):
        """Simula cachorro sentado"""
        print(self.name.title() + " is now sitting")

    def roll_over(self):
        """Simula cachorro rolar no chão"""
        print(self.name.title() + " roll over")


if __name__ == "__main__":
    tufik = Dog("tufik", 5)
    tufik.sit()
    tufik.roll_over()