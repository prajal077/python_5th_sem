print("prajal")

#This is simgle line comment

"""
    This is multi line comment
"""

#variables 

x = 10  #This is automatically integer
name = "prajal" #This is automatically string
bool = True

print(x, name, bool)


#getting the data type of a variable

print(type(x))
print(type(name))
print(type(bool))

#global variable
a = "awesome"
def myFunc () :
    print("Python is "+a)

myFunc()

#local variable of declared inside a function or a certain scope

def func2() :
    local = "locVariable"
    print("This is " +local)

func2()

#Example of few data types

# 1: Complex
complex = 1j
print(complex)

# 2: list
list = ["apple", "ball", "cat"]
print(list)

# 3: tuple
tuple = ("ram", "shyam", "hari")
print(tuple)

# 4: range
ran = range(12)
print(ran)

bool = True
print(bool)

bytes = b"hello"
print(bytes)

#type comversion

x = 1
y = 1.2

a = float(x)
b = int(y)

print(a)
print(b)