Salary=int(input("Enter the salary "))
age = int(input("Enter the age "))
if(Salary>=20000 or age<=25):
    loan = int(input("Enter the loan amount "))
    if(loan>5000):
     print("Maximum loan amount is 50000")
    else:
     print("Sorry You are not eligible")
else:
    print("Sorry You are not eligible")
