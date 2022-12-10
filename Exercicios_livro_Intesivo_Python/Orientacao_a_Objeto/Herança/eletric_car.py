from car import Car, Battery

class EletricCar(Car):
    """Representa aspectos específicos de veículos elétricos."""

    def __init__(self, make, model, year):
        """Inicializa os atributos da classe-pai."""
        super().__init__(make, model, year)
        self.battery = Battery()

    def fill_gas_tank():
        """Carros elétricos não têm tanques de gasolina."""
        print("This car doesn't need a gas tank")



       


if __name__ == "__main__":
    my_tesla = EletricCar('tesla', 'model s', 2016)
    my_tesla.get_descripttive_name()
    my_tesla.battery.describe_batery()
    my_tesla.battery.get_range()
