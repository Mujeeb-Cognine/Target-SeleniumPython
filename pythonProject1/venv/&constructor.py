class calculator:
  n = 110
  #default constructor
  def __init__(self,a,b):
    print("Getting called automatically")
    self.ab = a
    self.ba = b
  def getdata(self):
    print("Executing as part of method")
  def addition(self):
    return self.ab + self.ba + calculator.n

obj = calculator(2,3)
obj.getdata()
print(obj.addition())


obj = calculator(20,30)
obj.getdata()
print(obj.addition())
