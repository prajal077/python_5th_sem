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


# inheritance => single level

class parent :
    def details(self) :
        print("This is parent")

class child(parent) :
    def details(self) :    
        super().details()
        print("This is child")

obj3 = child()
obj3.details()

# multiple inheritance

class car :
    def show(self) :
        print("This is car class")

class bike :
    def show(self) :
        print("This is bike class")

class child(car, bike) :
    def showmethods (self) :
        car.show(self)
        bike.show(self)
        print("This is child class")

objj = child()
objj.showmethods()


#multilevel inheritance

class A :
    def show(self) :
        print("This is class A")

class B(A) :
    def shows (self) :
        print("This is classs B")

class C(B) :
    def showss (self) :
        print("This is class C")

objB = B()
objB.show()
objB.shows()

objC = C()
objC.shows()
objC.showss()

#another example of  multithreading in python

class E :
    def show(self) :
        print("This is class E")

class F(E) :
    def shows (self) :
        print("This is classs F")

class G(F) :
    def showss (self) :
        print("This is class G")

objF = F()
objB.show()
objB.shows()

objG = G()
objG.shows()
objG.showss()

