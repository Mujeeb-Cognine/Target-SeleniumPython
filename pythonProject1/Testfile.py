# You are given a number n.
# The number n can be negative or positive.
# If n is negative, print numbers from n to 0 by adding 1 to n.
# If positive, print numbers from n-1 to 0 by subtracting 1 from n.
#
# Example:1 Input:n = 0Output:already Zero
# Example2: Input:n = 4Output:3 2 1 0
# Example3: Input:n = -3Output:-3 -2 -1 0

print('Enter a number:')
x = input()
print('Hello, ' + x)

n = -5
if n > 0:
    while n:
        n -= 1
        print(n, end=" ")
elif n < 0:
    while n <= 0:
        print(n, end=" ")
        n += 1
elif n == 0:
    print("already Zero")


# n = -5
# if n < 0:
#     print(n)
#     m = n
#     while m == 0:
#         print(m)
#         m += 1





