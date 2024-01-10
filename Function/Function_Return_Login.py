username = "kishore"
Password = "123"

Enter_username = input("Enter the Username : ")
Enter_Password = input("Enter the Password : ")


def login():
    if username == Enter_username and Password == Enter_Password:
        return True          # output should store in one variable so created a variable as "Input" and stored login function
    else:
        return False


Input = login()
print(Input)
