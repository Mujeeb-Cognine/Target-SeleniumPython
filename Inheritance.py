class Python:
    # attribute and method of the parent class
    name = ""
    def topics(self):
        print("Welcome to Python")
# inherit from Animal
class selenium(Python):
    # new method in subclass
    def intermediate(self):
        # access name attribute of superclass using self
        print("Welcome to selenium with python", self.name)
# create an object of the subclass
labrador = selenium()
# access superclass attribute and method
labrador.name = "Inheritance"
labrador.topics()
# call subclass method
labrador.intermediate()


#Method overriding

class Python:
    # attribute and method of the parent class
    name = ""
    def topics(self):
        print("Welcome to Python")
# inherit from Animal
class selenium(Python):
    # new method in subclass
    def topics(self):
        # access name attribute of superclass using self
        print("Welcome to selenium with python", self.name)
# create an object of the subclass
labrador = selenium()
# access superclass attribute and method
labrador.name = "Inheritance"
labrador.topics()


#using super() method

class Teacher:
    name = ""
    def subject(self):
        print("I like python")
class students(Teacher):
    def subject(self):
        super().subject()
        print("Python with inheritance")
labrador = students()
labrador.subject()