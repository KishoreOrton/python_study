# Allows Dup
#Any type of date can be store
#We can modify the list item
# list - []

#insert()
#append()
#extend()
#pop()



a = [1,2,3,4,5]
#Check the data type
print("To check the date type")
print(type(a))

#Print the list
print("Print the list")
print(a)

#Print the specific value
print("Print specific value index ", a[0])

# Adding the value to list
b = [1,2,3,4,5]
b.append(6)
print("Print the added number",b)

#Insert the value
c = [1,2,3,4,5]
c.insert(0,9)
print(c)

#Merge two list
watches = ['Casio', 'Seiko', 'Orient']
swiss_watches = ['Jaeger-LeCoultre', 'Omega', 'Patek Philippe']
watches.extend(swiss_watches)
print(watches)

#Remove the value
d = [1,2,3,4,5]
d.pop()
print("Remove the last",d)
d.pop(0)
print("Remove the specific index",d)

