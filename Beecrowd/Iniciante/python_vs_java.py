class Land:
    def __init__(self, widthland, lengthland):
        self.widthland = widthland
        self.lengthland = lengthland
        self.price_land = 200.0

    def price_meter_land(self):
        return self.widthland * self.lengthland

    def area_square_meters(self):
        return self.price_meter_land() * self.price_land


if __name__ == '__main__':
    land = Land(10.0, 30.0)
    print(f'AREA = {land.price_meter_land()}')
    print(f'PRICE = R${land.area_square_meters()}')
