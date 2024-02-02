# Addition
# Add 10 to argument a, and return the result:
x = lambda a, b: a * b
print(x(5, 6))
# Multiply argument a with argument b and return the result:
x = lambda a, b: a * b
print(x(5, 6))
# Summarize argument a, b, and c and return the result:
x = lambda a, b, c: a + b + c
print(x(5, 6, 2))


# using functions
def myfunc(n):
  return lambda a: a * n


mydoubler = myfunc(2)
print(mydoubler(11))


def myfunc(n):
  return lambda a: a * n


mytripler = myfunc(3)

print(mytripler(11))


def myfunc(n):
  return lambda a: a * n


mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))


def addition(n):
    return lambda a: a + n


addition_result = addition(5)

print(addition_result(9))
print(addition_result(20))



