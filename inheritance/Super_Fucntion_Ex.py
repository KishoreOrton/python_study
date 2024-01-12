class Parent:

    def __init__(self, name):
        self.name = name
        self.age = 30


class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

    def display_parent_age(self):
        print(f, "Parent age is {super().age}")


child = Child("Alice", 10)

child.display_parent_age()
