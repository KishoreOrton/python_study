# Method 1

class Person :
  def __init__(self):
    self.name = ""
    self.age = ""

p1 = Person()
p1.name = "Kishore"
p1.age = 19

print(p1.name)
print(p1.age)

# Method 2

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)
