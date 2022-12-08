class Car:
    """Uma tentativa simples de representar um carro."""
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0


    def get_descripttive_name(self):
        """Devolve um nome descritivo, formatado de modo elegante."""
        print(f"\n{str(self.year)} {self.make} {self.model}")
        return

    def read_odometer(self):
        """Exibe uma frase que mostra a milhagem do carro."""
        print(f"This car has {self.odometer_reading} miles on it")

    def update_odometer(self, mileage):
        """Define o valor de leitura do hodômetro com o valor especificado."""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print(f"You can't roll back odometer")

    def increment_odomenter(self, miles):
        """Soma a quantidade especificada ao valor de leitura do hodômetro."""
        self.odometer_reading += miles

if __name__ == "__main__":
    my_new_car = Car('audi', 'a4', 2016)
    my_new_car.get_descripttive_name()
    my_new_car.update_odometer(70)
    my_new_car.update_odometer(40)
    my_new_car.read_odometer()

    my_used_car = Car('subaru', 'outback', 2013)
    my_used_car.get_descripttive_name()
    my_used_car.update_odometer(23500)
    my_used_car.increment_odomenter(500)
    my_used_car.read_odometer()