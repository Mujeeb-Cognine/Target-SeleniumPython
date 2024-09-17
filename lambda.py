y=(lambda x : x * 2)
print(y(3))

# how to use lambda functions with iterables
# filter()
# List
ages = [5, 12, 17, 18, 24, 32]
def myFunc(m):
  if m < 18:
    return False
  else:
    return True
adults = filter(myFunc, ages)
for m in adults:
  print(m)

  # how to use lambda functions with iterables
  # map()

def mycomp(a, b):
  return a + b
k = map(mycomp, ('apple', 'banana', 'cherry'), ('orange', 'lemon', 'pineapple'))
# print(k)
#   # convert the map into a list, for readability:
print(list(k))

# #closures
def greet():
  # variable defined outside the inner function
  name = "Thanu"
  # return a nested anonymous function
  return lambda: "Hi " + name
# call the outer function
message = greet()
# call the inner function
print(message())
#
#
# Using lambda() Function with reduce()
# A sum of all elements in a list using lambda and reduce() function
from functools import reduce
li = [5, 8, 10, 20, 50, 100]
sum = reduce((lambda x, y: x + y), li)
print(sum)          # Output is 193

# Find the maximum element in a list using lambda and reduce() function
import functools
 # Output is The maximum element of the list is : 6

from functools import reduce
# Here's a list of strings
words = ['Python', 'Reduce', 'Function', 'Tutorial']
# We'll try to use reduce to find the product of these strings
try:
    result = reduce((lambda x, y: x * y), words)
except TypeError as e:
    print(e)

#Clouser is a nested function:
def functionA(name):
  name = "New name"
  def functionB():
    print(name)
  return functionB
myfunction = functionA("")
myfunction()

#nonlocal keyword is using in clouser to modify an immutable variable present in the scope of outer variable
def functionA():
  counter = 0
  def functionB():
    nonlocal counter
    counter += 1



    return counter
  return functionB
myfunction = functionA()
retval = myfunction()
print("Counter:", retval)
retval = myfunction()
print("Counter:", retval)
retval = myfunction()
print("Counter:", retval)
retval = myfunction()
print("Counter:", retval)