# In Python, function is a group of related statements that performs a specific task.
# Function Declaration
def demo(name):
    print("Learning functions" + name)
    # Function Call


def addIntegers(a, b):
    return a+b


demo("Anupama")
print(addIntegers(2,10))

# Fibnonacci Number


def Fibonacci(n):
     if n < 0:
        print("Incorrect input")
     elif n == 0:
        return 0
     elif n == 1 or n == 2:
        return 1
     else:
        return Fibonacci(n - 1) + Fibonacci(n - 2)
print(Fibonacci(9))
