class MyClass:
    x = 5


print(MyClass)


# Now we can use the class named MyClass to create objects:
p1 = MyClass()
print(p1.x)

# The __init__() Function
# All classes have a function called __init__(), which is always executed when the class is being initiated.
# Use the __init__() function to assign values to object properties,
# or other operations that are necessary to do when the object is being created:


class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age


p1 = Person("Manasa", 11)

print(p1.name)
print(p1.age)

# The __str__() Function


class manasa:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name}({self.age})"


p1 = manasa("Manasa", 12)

print(p1)


