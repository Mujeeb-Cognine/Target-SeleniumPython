# Dictionary
Car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(Car)

# Print the "brand" value of the Car dictionary
Car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(Car["brand"])

# Duplicate values will overwrite existing values
Car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(Car)

# Print the length/number of items in the dictionary
print(len(Car))

#  The values in dictionary items can be of any data type: String, int, boolean, and list
Cars = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
print(Cars)

# Print the datatype of a dictionary
print(type(Car))
print(type(Cars))

# It is also possible to use the dict() constructor to make a dictionary.
CabDriver = dict(name="John", age=36, country="Norway")
print(CabDriver)

# Dictionary

myfamily = {
    "child1": {
        "name": "Ema1",
        "year": 2004
    },
    "child2": {
        "name": "Tobias4",
        "year": 2007
    },
    "child3": {
        "name": "Linu3",
        "year": 2011
    }
}

print(myfamily)


# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered, unchangeable*, and un indexed. No duplicate members.
# Dictionary is a collection which is ordered** and changeable. No duplicate members.

