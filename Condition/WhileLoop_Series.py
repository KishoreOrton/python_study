# Get the series 10,20,30,40.....200

i = 10
while i < 200:
    print(i, end=",")
    i = i + 10

print()

# Print 1st 10 Natural number

j=10
while j>0:
    print(j, end=",")
    j = j - 1

# Factorial
print()

k=int(input("Give me the factorial number = "))
fact = 1
while(k>0):
    fact=fact*k
    k=k-1
print(fact)
