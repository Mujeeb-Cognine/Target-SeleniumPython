### The Second Heighest Number in a List####
def second_highest(numbers):
    if len(numbers) < 2:
        raise ValueError("List must contain at least two numbers.")
    unique_numbers = list(set(numbers))
    if len(unique_numbers) < 2:
        raise ValueError("List must contain at least two distinct numbers.")
    unique_numbers.sort(reverse=True)
    return unique_numbers[1]
numbers = [1, 8, 4, 6, 8, 10]
print("The Second Heighest Number is",second_highest(numbers))

####### Even or Odd ########
num = int(input("Enter a number: "))
if (num % 2) == 0:
   print("{0} is Even".format(num))
else:
   print("{0} is Odd".format(num))
