class phone:
    def __init__(self, brand, price, chargertype):
        self.brand = brand
        self.price = price
        self.charger = chargertype

    def displayphone(self):
        print("Brand = ", self.brand)
        print("price = ", self.price)
        print("Charger = ", self.charger)


iphone = phone("iPhone", 79000, "Lightingcable")
iphone.displayphone()

Oneplus = phone("One+", 35000, "C-Type")
Oneplus.displayphone()
