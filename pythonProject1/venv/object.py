# Object Methods

# Objects can also contain methods. Methods in objects are functions that belong to the object.
# Let us create a method in the Person class:
# Example - Insert a function that prints a greeting, and execute it on the p1 object:

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)


p1 = Person("Manasa", 13)
p1.myfunc()


# Modifing the Object properties

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)


p1 = Person("Manasa", 14)
p1.age = 15
print(p1.age)
# Delete Object Properties
del p1.age
print(p1.age)

