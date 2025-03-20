# #class
# objects
# methods
# self - > This
# dunder methods - > constructor

class Colony :
    house = 10
    name = "prajal"

house1 = Colony()
print(house1.house)
print(house1.name)

house2 = Colony()
house2.name = "ram"
print(house2.name)    #changing the values of class through  object



#constructor

class Kist :
    def __init__(self, batch, name):
        self.batch = batch
        self.name = name

        print(f"name = {name},  batch = {batch}")

student = Kist("fifth", "prajal")

class add :
    def __init__(self, a, b) :
        self.a = a
        self.b = b
        print(a+b)

obj = add(2, 3)


#static class and static methods

class One :
    @staticmethod
    def abc(a, b) :
        return a + b

print(One.abc(4, 5))

class Two :
    @classmethod
    def cdf(cls, a, b) :
        cls.a = a
        cls.b = b
        print(a+b)

Two.cdf(5, 5)

#wap to make class named STUDENTS with the attributes need to make the constructor with values name, age, gender, and batch.
# make 3 methods where the 1st method give the sum of 2 number, 2nd method print the name, age and the last method print gender and batch

class Students :
    def __init__(self, name, age, gender, batch):
        self.name = name
        self.age = age
        self.gender = gender
        self.batch = batch

    def add (self, a, b) :
            print(a+b)

    def second (self) :
        print(f"name = {self.name}, age = {self.age}")

    def third (self) :
        print(f"gender = {self.gender}, batch = {self.batch}")


student1 = Students("Prajal", 20, "Male", "Fifth")
student1.add(3, 3)
student1.second()
student1.third()
            