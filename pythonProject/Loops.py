name = " Anupama Saranu"
a=10

if a > 2:
    print("condition matches")
else:
    print("condition not matches")

print("if else condition code is completed")

# elif loop

person_age = 21

if person_age >= 18:
    print("Eligible for voting")
elif person_age < 10:
    print("Not eligible for voting")
elif person_age == 10:
    print("Minor")
else:
    print("Invalid Age")

# For loop

obj=[2,3,4,5]
for i in obj:
    print(i*2)

# Sum of first natural numbers 1+2+3+4+5
# range(i,j) - > i,j-1
summation = 0
for j in range(1,6):
    summation = summation + j
print(summation)

print("***************************")
# Jumping 2 iterations(Passing index)
for k in range(1,10,2):
    print(k)

print("***************")
# Skipping the first index
for m in range(10):
    print(m)