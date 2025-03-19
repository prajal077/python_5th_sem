#functions

def add () :
    print(5+5)
add ()

def multiply (a, b) :
    return a*b

a = 10
b = 20

def div () :
    return b/a
print(div())

# parameters in function

def fun (a, b) :
    print(a+b)
fun(4, 5)

# even number using function and passing range as a parameter

def even (a, b):
    for i in range (a, b) :
        if i % 2 == 0 :
            print(i)
        else :
            pass

even (0, 11)