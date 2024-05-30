def rest(func):
    # define the inner function
    def inner():
        # add some additional behavior to decorated function
        print("I need to take rest")
        # call original function
        func()

    # return the inner function
    return inner


# define ordinary function
@rest
def sleep():
    print("I am going to sleep")

sleep()


# decorate the ordinary function
# decorated_func = rest(sleep)
# call the decorated function
# decorated_func()


def make_pretty(func):
    def inner():
        print("I got decorated")
        func()

    return inner

@make_pretty
def ordinary():
    print("I am ordinary")

ordinary()


def calculation():
    num = 1

    def inner_fun():
        nonlocal num
        num += 5
        return num

    return inner_fun


odd = calculation()
print(odd())
print(odd())
print(odd())
odd2 = calculation()
print(odd2())


# Decorator is a function that receives another function as argument.

def my_function(x):
    print("The number is=", x)


def my_decorator(some_function, num):
    def wrapper(num):
        print("Inside wrapper to check odd/even")
        if num % 2 == 0:
            ret = "Even"
        else:
            ret = "Odd!"
        some_function(num)
        return ret

    print("wrapper function is called")
    return wrapper


no = 10
my_function = my_decorator(my_function, no)
print("It is ", my_function(no))


# Recursion : A function that calls itself
def factorial(n):
    if n == 0:
        print(n)
        return 0
    else:
        print(n, '*', end=' ')
        return n * factorial(n - 1)


print('factorial of 0=', factorial(0))

# Implicit casting
a = True
b = 10.5
c = a + b
print(c)

# Explicit Casting
a = int(10.5)
print(a)
g = int(2.3 * 14)
print(g)
print(type(g))
