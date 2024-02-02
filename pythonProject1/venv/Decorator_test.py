# Closures are often used to implement data encapsulation and maintain the state between function calls.
# Decorators:
# A decorator is a way to modify the behavior of a function or a class without directly changing its source code.
# Python program to illustrate functions can be treated as objects
def shout(text):
    return text.upper()


print(shout('Hello'))
yell = shout
print(yell('Hello'))


# In the above example, we have assigned the function shout to a variable.
# This will not call the function instead it takes the function object referenced by a shout and
# creates a second name pointing to it, yell.
##################################################
# Python program to illustrate functions
# can be passed as arguments to other functions
def shout(text):
    return text.upper()


def whisper(text):
	return text.lower()


def greet(func):
	# storing the function in a variable
	greeting = func("""Hi, I am a String created by a function passed as an argument.""")
	print(greeting)


greet(shout)
greet(whisper)

########################################################################
def my_decorator(func):
	def wrapper():
		func()
		print("Something is happening before the function is called.")
		func()
		print("Something is happening after the function is called.")
		func()

	return wrapper


@my_decorator
def say_hello():
	print("Hello!")


say_hello()

##########################################################################

# Python program to illustrate functions
# Functions can return another function

def create_adder(x):
	def adder(y):
		return x+y

	return adder

add_15 = create_adder(15)

print(add_15(10))



