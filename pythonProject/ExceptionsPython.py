ItemInCart = 0
# 2 items will be added in the cart

# if ItemInCart != 2:
#     raise Exception("Products cart count not matching")

assert(ItemInCart == 0)


# try, Catch

try:
    with open('filelog.txt', 'r') as reader:
        reader.read()

except:
    print("Try catch demo")

try:
    with open('filelog.txt', 'r') as reader:
        reader.read()

except Exception as e:
    print(e)