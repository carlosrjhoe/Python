class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age


    def presentation(self):
        print(f"My dog's name is, {self.name.title()}")
        print(f"My dog's age is, {self.age}, years old")

    def sit(self):
        """Simula cachorro sentado"""
        print(f"{self.name.title()} is now sitting")

    def roll_over(self):
        """Simula cachorro rolar no chão"""
        print(f"{self.name.title()}, roll over")


if __name__ == "__main__":
    tufik = Dog("tufik", 5)
    tufik.presentation()
    tufik.sit()
    tufik.roll_over()