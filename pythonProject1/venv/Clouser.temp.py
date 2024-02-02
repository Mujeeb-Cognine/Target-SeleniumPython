# Python program for nested functions
def outerFunction(text):

	def innerFunction():
		print(text)

	innerFunction()


if __name__ == '__main__':
	outerFunction('Hey!')


def outer_function(x):
	def inner_function(y):
		return x + y

	return inner_function


# Create a closure
closure_example = outer_function(5)

# Using the closure
result = closure_example(3)  # This will add 5 (from outer_function) + 3
print(result)  # Output will be 8

# Python program to illustrate
# closures
import logging

logging.basicConfig(filename='example.log',
					level=logging.INFO)


def logger(func):
	def log_func(*args):
		logging.info(
			'Running "{}" with arguments {}'.format(func.__name__,
													args))
		print(func(*args))

	# Necessary for closure to
	# work (returning WITHOUT parenthesis)
	return log_func


def add(x, y):
	return x + y


def sub(x, y):
	return x - y


add_logger = logger(add)
sub_logger = logger(sub)

add_logger(3, 3)
sub_logger(20, 10)
add_logger(4, 5)
sub_logger(10, 5)

