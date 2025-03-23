# polymorphism

class Cat :
    def speak(self) :
        print("cat meows")

class Dog :
    def speak(self) :
        print("Dog Barks")

obj = [Cat(), Dog()]

for i in obj :
    i.speak()

# exceptional handling

try :
    print(x)
except Exception as e :
    print("error")
else :
    print("not error")
finally :
    print("This is finally block")


try :
    a
except NameError as e :
    print("Name error")
else :
    print("not error")

# API fetching

