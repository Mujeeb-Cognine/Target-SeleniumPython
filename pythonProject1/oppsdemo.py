class calculator:

    num = 100

    def __init__( self, a, b):
        self.number1 = a
        self.number2 = b
        print("I am called automatically")

    def getdata(self):
        print("Called as part of a method")

    def summation(self):
        return self.number1 + self.number2 + calculator.num

obj = calculator(10,20)
obj.getdata()
print(obj.summation())