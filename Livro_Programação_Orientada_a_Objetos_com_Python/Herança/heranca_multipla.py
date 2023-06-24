class Merchandise:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Meat(Merchandise):
    def __init__(self, type, weight):
        self.type = type
        self.weight = weight

class Utensils:
    def __init__(self, skewrs, coal):
        self.skewrs = skewrs
        self.coal = coal

class BarbecueKit(Meat, Utensils):
    """Herança multipla: Se dá quando uma classe é dona de outra pela interligação de seus atributos e a forma sequencial como uns dependem dos outros."""
    pass

if __name__ == '__main__':
    package = BarbecueKit('carne', 14.90)
    package.type = 'costela'
    package.skewrs = 1
    package.coal = 1

    print(f'{package.type}\n{package.weight}\n{package.skewrs}\n{package.coal}')