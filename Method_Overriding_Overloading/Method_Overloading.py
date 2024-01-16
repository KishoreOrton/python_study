# Method Overloading is a fundamental concept in OOP that enables a class to define multiple methods with the same name but different parameters. In Python, this powerful feature allows developers to create versatile functions capable of handling various data types.
# It also helps perform distinct operations based on the types and number of arguments passed


class MathOperations:

    def add(self, a, b):
        return a + b

    def add(self, a, b, c):
        return a + b + c

    def add(self, a, b, d):
        return a + b + d

Oper = MathOperations()
print(Oper.add(1,2,7))


class MyClass:
    def my_method(self, arg1, arg2=0):
        if arg2:
            print(arg1 + arg2)
        else:
            print(arg1)


# Calling the method with one argument
obj = MyClass()
obj.my_method(10)

# Calling the method with two arguments
obj.my_method(10, 20)
