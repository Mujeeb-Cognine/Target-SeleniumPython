# Classes are user defined blueprint or prototype
# sum, multiplication, addition, constant
# methods, class variables, instance variables, constructor etc..
# Objects for your classes-


# Class and methods and calling the methods and variables using objects
class Calculator:
    num = 100

    def getData(self):
        print("I am now executing as method in class")


obj = Calculator() # Syntax to create objects in python
obj.getData()
print(obj.num)
print("----------------------------------------------------------------")

# Calling self constructor
# Two Variables - 1) Class variable 2) Instance Variable
# Class variables will be constant no matter how many objects we create
# Variables which are defined inside constructor are called instance variables
# The number of arguments passed in class , same number of arguments should also be passed in the constructor
# self is an object, the obj passed as first argument to self
# self keyword is madatory for calling variables names in methods
# Constructor name should be  __init__
# new keyword  is not required when you create object

class Calculator1:
    num1 = 1000 #Class variable
    # Default constructor

    def __init__(self, a, b):
        self.firstNumber= a #Instance variables
        self.secondNumber= b
        print("I am called automatically when object is created")

    def getData1(self):
        print("I am now executing as method in class")

    def Summation(self):
        return self.firstNumber + self.secondNumber + Calculator1.num1
        # Calling variables with self. in the methods --Mandatory in python

# Parameterised constructor
obj1 = Calculator1(2,3)
obj1.getData1()
print(obj1.Summation())
print(obj1.num1)

obj3 = Calculator1(4,5)
obj3.getData1()
print(obj3.Summation())
print(obj3.num1)

# Non-Parameterised constructor
# obj2 = Calculator1()
# obj2.getData1()
# print(obj2.num1)