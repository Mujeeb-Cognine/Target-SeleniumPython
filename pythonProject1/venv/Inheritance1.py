# Consider this as parent class
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

# Use the Person class to create an object, and then execute the printname method:


x = Person("Manasa", "Chamarthi")
x.printname()


# Consider Student as the child class - inheritance
# pass
# we can use the pass when there is no statement to pass
# To keep the inheritance of the parent's __init__() function, add a call to the parent's __init__() function:
# Python has a super() function that will make the child class inherit all the methods and properties from its parent:
class Student(Person):
  def __init__(self, fname, lname, Language):
    # Person.__init__(self, fname, lname)
    super().__init__(fname, lname)
    self.LanguageLearning = Language  #  Adding the properties to the child class

  def note(self):
    print(self.firstname, self.lastname, "is learning", self.LanguageLearning)


x = Student("Chamarthi", "Manasa", "Python")
x.printname()
print(x.LanguageLearning)
x.note()
