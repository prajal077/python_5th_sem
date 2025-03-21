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

#wap to add 3 numbers using encapsulation. make the 2 values private. chnage the value and then add

class add :
    def __init__(self, a, b, c):
        self.a = a
        self.__b = b
        self.__c = c

    def info(self) :
        print(f"a = {self.a}, b = {self.__b}, c = {self.__c}")

    def chanfv(self, a, b, c) :
        self.a = a
        self.__b = b
        self.__c = c    

        print(f"a = {self.a}, b = {self.__b}, c = {self.__c}")
        print(self.a + self.__b + self.__c )

        

obj1 = add(1, 2, 3)
obj1.info()

obj1.chanfv(4, 5, 6)



#ABSTRACTION

from abc import ABC, abstractmethod
class Car(ABC) :
    @abstractmethod
    def details(self) :
        pass

class Ford(Car) :
    def details(self) :
        print("car is ford")

obj2 = Ford()
obj2.details()