def fun1(z):
    def fun2(x,y):
        x = 25
        z = x+y
        print(z)

        return fun2(25, 27)

fun1(2)

