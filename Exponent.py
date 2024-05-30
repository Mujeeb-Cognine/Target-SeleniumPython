x=1
while(x<10):
    print(x ** 2,end="\n")
    x=x+1
print(id(x))
# #
# def add(a,b):
#     print(a+b)
# add(2,3)
# #
# def add(a,b):
#     return a+b
# c=input(add(12,3))
#
# # def add(t,k):
# #     return t+k
# # print(add(25,3))
#
# #
# # num=54
# # temp=num
# # sum=0
# # while temp > 0:
# #     d=temp % 10
# #     sum+=d ** 3
# #     temp=temp//10
# # if num  == sum:
# #     print("It is an amstrong number")
# # else:
# #     print("Not an amstrong")
# #
# #
# # import sys
# # string="Thanusha"
# #
# # sys.getsizeof(string)
#
# #
# # text="Hello Thanu"[::-1]
# # print(text)
#
#
# ##the number and second element as the cube of the number.
list1 = [1, 2, 5, 6]

# using list comprehension to iterate each
# values in list and create a tuple as specified
res = [(val, pow(val, 3)) for val in list1]
print(res)

# rows = int(input("Enter number of rows: "))
#
# for i in range(rows):
#     for j in range(i+1):
#         print("* ",end="")
#     print("\n")


rows = int(input("Enter number of rows: "))

for i in range(rows, 0, -1):
    for j in range(0, i):
        print("* ", end=" ")

    print("\n")




it.product="IT Product"
it.consulting="IT Consulting"


def dec(func):
    def inner():
        print("Hello world")
        func()
def clo():
    print("Hello")












