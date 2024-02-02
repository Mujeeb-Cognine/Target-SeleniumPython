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
