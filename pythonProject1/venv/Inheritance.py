from constructor import calculator

class child12(calculator):
    n2 = 150

    def __init__(self):
        calculator.__init__(self,15, 30)

    def getCompleteData(self):
        return self.n + self.n2 + self.addition()

obj = child12()
print(obj.getCompleteData())

