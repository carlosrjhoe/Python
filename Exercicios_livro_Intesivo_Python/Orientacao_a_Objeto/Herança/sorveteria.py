from restaurante import Restaurant

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name,  cuisine_type, number_served):
        super().__init__(restaurant_name,  cuisine_type, number_served)



if __name__ == "__main__":
    sorveteria = IceCreamStand('Sorveteria da Luna', 'Sorveteria', 0)
    sorveteria.describe_restaurant()
    sorveteria.open_restaurant()
    sorveteria.read_served()
    sorveteria.set_number_served(15)
    sorveteria.read_served()