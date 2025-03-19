#functions

# def add () :
#     print(5+5)
# add ()

# def multiply (a, b) :
#     return a*b

# a = 10
# b = 20

# def div () :
#     return b/a
# print(div())

# # parameters in function

# def fun (a, b) :
#     print(a+b)
# fun(4, 5)

# # even number using function and passing range as a parameter

# def even (a, b):
#     for i in range (a, b) :
#         if i % 2 == 0 :
#             print(i)
#         else :
#             pass

# even (0, 11)

# # odd number using function and passing range as a parameter

# def odd (a, b):
#     for i in range (a, b) :
#         if i % 2 != 0 :
#             print(i)
#         else :
#             pass

# odd (0, 11)

#function types
# 1. no parameter with no return type
# 2. with parameter with return type

def name (a, b) :
    print(a+b)

name("prajal", " bhattarai")


#types of paramter in python

# default
# named
# *args
# **kwargs
# positional arguments

# default

def default (name, age = 20) :  # it is default as age is predefined in the argument. If we pass the value forcefully, it will overwrite the default value else, the default value if printed

    print(f"name = {name} and age = {age}")

default("prajal", 22)
default("prajal")


#named

def named (name, age) :
    print(f"name = {name} and age = {age}")

named("Ram", 10)
named(10, "Ram")   # jasto order ma value pathako cha testai aaucha


# *args

def args (name) :
    for i in name :
        print(name)

args("shyam")