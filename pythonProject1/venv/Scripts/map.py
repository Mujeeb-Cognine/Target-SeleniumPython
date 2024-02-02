
def myfunc(a):
  return len(a)


x = map(myfunc, ('apple', 'banana', 'cherry'))
print(x)
# convert the map into a list, for readability:
print(list(x))


def myfunc(a, b):
  return a + b


x = map(myfunc, ('apple', 'banana', 'cherry'), ('orange', 'lemon', 'pineapple'))
print(x)
print(list(x))


