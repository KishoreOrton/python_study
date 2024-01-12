class phone:
    charger = "C-type"                  # Class variable

    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def displayphone(self):
        print("Brand = ", self.brand)
        print("price = ", self.price)
        print("Charger = ", self.charger)


Display = phone("iPhone", 79000)
Display.displayphone()
