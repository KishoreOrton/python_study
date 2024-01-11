class Laptop:
    price = ""
    processor = ""
    ram = ""


HP = Laptop()
DELL = Laptop()

HP.price = 50000
HP.processor = "i3"
HP.ram = "8GB"

DELL.price = 70000
DELL.processor = "i5"
DELL.ram = "12GB"

# Without class and objects
print(HP.price)
