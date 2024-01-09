# Do not allow duplicate , duplicate values will be removed
# Any data type can be stored
# Key:Value {"Name":"kishore"}

# get(),keys(),items(),update(),thisdict(),thisdict.pop()

# Print the values
a = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(a)

# Print the specific value by keys
b = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(b["brand"])

# Will not allow duplicates so last value will print
c = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "year": 2020
}
print(c)

# Multiple values can be given
d = {
    "brand": "Ford",
    "electric": False,
    "year": 1964,
    "colors": ["red", "white", "blue"]
}

print(d)
