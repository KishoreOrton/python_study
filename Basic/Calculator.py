Num1 = int(input("Enter number 1 = "))
Num2 = int(input("Enter number 2 = "))
Operation = input("Choose the operation - Add/Sub/Div/Mul = ")

if (Operation == "Add"):
        print(Num1+Num2)
elif (Operation == "Sub"):
        print(Num1-Num2)
elif (Operation == "Div"):
        print(Num1/Num2)
elif (Operation == "Mul"):
        print(Num1*Num2)
else:
    print("Invalid Operator")
