#conditions
if True:
    print("True")
else :
    print("Flase")

#wap to check if the user is above 18 or not
# age = 18
# if(age>18):
#     print("User is above 18")
# else:
#     print("User is below 18")

# #match (x) case
# num = int(input("Enter a number: "))
# match num:
#     case 1:
#         print("The entered number is 1")
#     case 2:
#         print("The entered number is 2")
#     case _:
#         print("invalid input")

#wap to check whether the given character is vowel or not

vowel = input("Enter a charecter to check whether it is vowel or nor: ")
match vowel :
    case 'a' :
        print("This is vowel a")
    case 'e' :
        print("This is vowel e")
    case 'i' :
        print("This is vowel i")
    case 'o' :
        print("This is vowel o")
    case 'u' :
        print("This is vowel u")
    case _:
        print("This is not vowel")