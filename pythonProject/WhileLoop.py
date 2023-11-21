a = 4
while a > 1:
    if a != 4:
        break
    print(a)
    a = a - 1

print('while loop execution is done')

# program to print odd numbers from 1 to 10

num = 0

while num < 10:
    num += 1

    if (num % 2) == 0:
        continue

    print(num)