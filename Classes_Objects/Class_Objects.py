class goa:

    name = ""                              # Variable in the class
    drink = ""

    def party(self):                       # Function in the class
        print("Lets party")
    def beach(self):
        print("Enjoy the beach")

kishore = goa()                            # Created a object to store the class
Ragul = goa()

kishore.party()                            # Calling the fucntion from the class by object.function()
Ragul.beach()

kishore.name = "Kishore"                   # Object and calling the class variable
Ragul.drink = "Kingfisher"

print(kishore.name)
print(Ragul.drink)
