def Narutoseries(Naruto):
  print(Naruto + " Welcome")

Narutoseries("Toby")
Narutoseries("Naruto")
Narutoseries("Hinata")


def Narutoseries1(Hero, Heronie):
  print(Hero + " LOVES " + Heronie)

Narutoseries1("Naruto", "Hinata")

#Arbitrary Arguments, *args
#This way the function will receive a tuple of arguments, and can access the items accordingly:

def my_function(*kids):
  print("The youngest child is " + kids[1])

my_function("Emil", "Tobias", "Linus")

# Keyword Arguments
def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")   # Key and value we can give key to get value
