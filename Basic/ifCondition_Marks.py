from statistics import mean

English = int(input("English = "))
Tamil = int(input("Tamil = "))
Maths = int(input("Maths = "))
Science = int(input("Science = "))
Social = int(input("Social = "))

Total_Marks = (English, Tamil, Maths, Science, Social)
average = mean(Total_Marks)

print("Average: ", round(average))

average = round(average)

if(average<35):
    print("Additional call required ")
else:
    print("You are good to go")
