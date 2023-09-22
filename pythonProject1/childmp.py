from oppsdemo import calculator

class childimpl(calculator):

    num2 = 200

    def __init__(self):
        # print(num2)
        calculator.__init__(self,2,10)
    def getcompletedata(self):
        return self.num + self.num2 + self.summation()


obj = childimpl()
print(obj.getcompletedata())
