# using this module2 for testing purpose, this file uses the data of modules.py(by import)
# Import the module named mymodule, and call the greeting function:
import modules
# imported the file in system
import platform
# imported the built-in module - platform
from modules import person1
# imported person1 from the modules

modules.greeting("Python")

# getting one of the variables from a list

Name = modules.person1["First name"]
print(Name)

x = platform.system()
print(x)

# There is a built-in function to list all the function names (or variable names) in a module. The dir() function:

AllNames = dir(modules)
print(AllNames)

# Import From Module
# You can choose to import only parts from a module, by using the from keyword.
# The module named modules has one function and one dictionary:

print(person1["country"])


