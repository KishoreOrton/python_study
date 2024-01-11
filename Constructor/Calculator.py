class Calculator:
    def __init__(self):
        self.num1 = ""
        self.num2 = ""

    def add(self):
        print("add", self.num1+self.num2)

    def sub(self):
        print("sub", self.num1-self.num2)

Number = Calculator()
Number.num1 = 10
Number.num2 = 2

Number.add()
Number.sub()
