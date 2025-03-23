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