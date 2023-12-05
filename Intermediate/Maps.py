def my(a):
  return len(a)
x = map(my, ('1234', 'apple', 'cherry'))

print(x)
print(list(x))
