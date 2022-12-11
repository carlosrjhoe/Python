from restaurante import Restaurant

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name,  cuisine_type, number_served):
        super().__init__(restaurant_name,  cuisine_type, number_served)
        self.flavors = [
            'flocos',
            'chocalate',
            'napolitano',
            'brigadeiro'
        ]

    def describe_flavors(self):
        print(f'Nossos sabores de sorvete são:')
        for i, sabor in enumerate(self.flavors):
            print(f'{i+1} - {sabor.title()}')


if __name__ == "__main__":
    sorveteria = IceCreamStand('Sorveteria da Luna', 'Sorveteria', 0)
    sorveteria.describe_restaurant()
    sorveteria.open_restaurant()
    sorveteria.describe_flavors()
    sorveteria.set_number_served(15)
    sorveteria.read_served()