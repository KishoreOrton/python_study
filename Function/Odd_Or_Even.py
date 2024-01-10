def Odd_Or_Even():
    if int(num) % 2 == 0:
        print("Even")
    else:
        print("Odd")


num = int(input("Enter the number to find odd or even "))
Odd_Or_Even()

# Method 2

def Odd_Or_Even_Method2(a):  # value b is now stored as arg a
    if int(a) % 2 == 0:
        print("Even")
    else:
        print("Odd")


b = int(input("Enter the number to find odd or even "))
Odd_Or_Even_Method2(b)   # User input stored in b , now value in b is now arg in a now a = user input

