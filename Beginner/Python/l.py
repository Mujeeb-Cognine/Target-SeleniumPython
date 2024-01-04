# import sys
#
# text = ("Vamsi", "Krishna")
#
# print(str(sys.getsizeof(text)))


import sys

test = "ab"

print("The original string : " + str(test))

res = sys.getsizeof(test)

print("The length of string in bytes : " + str(res))
