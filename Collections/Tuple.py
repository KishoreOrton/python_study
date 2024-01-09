# Allows dup
# Any type of data type can be stored
# Cant modify
# Tuple - ()

a=(1,2,3,4,5)
print(a)

# We can't modify the tuple so we can casting

x=(1,2,3,4,5)
y=list(x)
print(y)   # o/p [1,2,3,4,5]

# Tuple is changed to list now we can modify
y.append(6)
y.append(7)
y.pop(0)
print(y)
