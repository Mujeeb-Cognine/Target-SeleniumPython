# Inheritance is child acquiring properties from parent class

# 1)Calling parent in class
# 2)Importing the parent
# 3)If there is constructor no default, then make sure to call parent constructor

from OopsDemo import Calculator1


class ChildImp1(Calculator1):
    num2 = 200

    def __init__(self):
        Calculator1.__init__(self,2,10)

    def getCompleteData(self):
        return self.num2 + self.num1 + self.Summation()


obj = ChildImp1()
print(obj.getCompleteData())
