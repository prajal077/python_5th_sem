# encapsulation

class Encap :
    def __init__(self, a, b, c):
        self.a = a      #public
        self._b = b     #protected
        self.__c = c     #private

    def getInfo (self) :
        print(f"a = {self.a}, b = {self._b}, c = {self.__c}")
        
    #changing the value in getInfo function
    def change(self, c):
        self.__c = c 
            
obj = Encap(10, 20, 30)
obj.getInfo()

print(obj.a)
print(obj._b)
# print(obj.__c)    This cause error cause we cannot access the private variable from outside the function

obj.change(50)
obj.getInfo()