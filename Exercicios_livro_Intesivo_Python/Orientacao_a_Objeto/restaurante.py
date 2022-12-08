class Restaurant:
    def __init__(self, restaurant_name,  cuisine_type, number_served):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0


    def describe_restaurant(self):
        """Imforma descrição do restaurante"""
        print(f"Tipo de restaurante:\n{self.cuisine_type}")
        return

    def open_restaurant(self):
        """Informa que o restaurante está aberto"""
        print("O restaurante",self.restaurant_name,"esta aberto.")
        return

    def read_served(self):
        """Informativo de quantas pessoas estão sendo atendidas"""
        print(f"Estamos atendendo {self.number_served} pessoas")

    def set_number_served(self, served):
        """Modifica a quantidade de clientes"""
        self.number_served = served


if __name__ == "__main__":
    restaurante = Restaurant("Bolos da May", "Confeitaria", 10)
    restaurante.describe_restaurant()
    restaurante.open_restaurant()
    restaurante.set_number_served(20)
    restaurante.read_served()
    restaurante.set_number_served(30)
    restaurante.read_served()
    