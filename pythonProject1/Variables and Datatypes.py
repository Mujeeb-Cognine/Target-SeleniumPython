# Python has no command for declaring a variable.
# A variable is created the moment you first assign a value to it.
x = 5
y = "John"
print(x)
print(y)

# Variables do not need to be declared with any particular type, and can even change type after they have been set.
x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)

# If you want to specify the data type of a variable, this can be done with casting.
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

# You can get the data type of a variable with the type() function.
x = 5
y = "John"
print(type(x))
print(type(y))

# String variables can be declared either by using single or double quotes:
x = "John"
# is the same as
x = 'John'
print(x)
print(type(x))

# Variable names are case-sensitive.
a = 4
A = "Sally"
# A will not overwrite a
# A variable name cannot be any of the Python keywords

myvar = "John"
my_var = "Jo"
_my_var = "Jon"
myVar = "ohn"
MYVAR = "Jhn"
myvar2 = "Joh"


print(myvar)
print(my_var)
print(_my_var)
print(myVar)
print(MYVAR)
print(myvar2)

# Python allows you to assign values to multiple variables in one line

K, L, M = "Orange", "Banana", "Cherry"
print(K)
print(L)
print(M)

# can assign the same value to multiple variables in one line

D = E = F = "Oranges"
print(D)
print(E)
print(F)

# Unpack a Collection
# If you have a collection of values in a list, tuple etc.
# Python allows you to extract the values into variables. This is called unpacking.

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

# Global Variables
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

# x = "awesome" is the Global Variable
# If there is no Declaration in the function then x = "awesome" is used,
# if there is a declaration in the function then x = "awesome" will be ignored and the declaration will be considered

