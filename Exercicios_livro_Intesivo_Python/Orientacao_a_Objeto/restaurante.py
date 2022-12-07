class Restaurant:
    def __init__(self, restaurant_name,  cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type


    def describe_restaurant(self):
        print("Tipo de restaurante:\n",self.cuisine_type)
        return

    def open_restaurant(self):
        print("O restaurante",self.restaurant_name,"esta aberto.")
        return


if __name__ == "__main__":
    restaurante = Restaurant("Bolos da May", "Confeitaria")
    restaurante.describe_restaurant()
    restaurante.open_restaurant()