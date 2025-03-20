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



