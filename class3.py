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

# vowel = input("Enter a charecter to check whether it is vowel or not: ")
# match vowel :
#     case 'a' :
#         print("This is vowel a")
#     case 'e' :
#         print("This is vowel e")
#     case 'i' :
#         print("This is vowel i")
#     case 'o' :
#         print("This is vowel o")
#     case 'u' :
#         print("This is vowel u")
#     case _:
#         print("This is not vowel")

#wap using match case to check what day is today

# day = int(input("Enter a number to check the day"))
# match day:
#     case 1:
#         print("Sunday")
#     case 2:
#         print("Monday")
#     case 3:
#         print("Tuesday")
#     case 4:
#         print("wednesday")
#     case 5:
#         print("Thrusday")
#     case 6:
#         print("Friday")
#     case 7:
#         print("Saturday")
#     case _:
#         print("invalid input")

#loops
 # last ko value chai print hudaina or lidaina

# for i in range (0, 5):
#     print(i)

# a = 0
# while a<10 :
#     print(a)
#     a+=1

#break

# for i in range (0, 5):
#     if i == 3 :
#         break
#     print(i)

# #continue

# for i in range (10, 20) :
#     if i == 15 :
#         continue
#     print(i)

# #wap to print table of 5
# for i in range (0, 11):
    print("5 *",i, "= ", 5*i )

#wap to check if the given number is light, fire or water. If the number is divisible by 5 it is light, if by 6 it is fire and if by 7 it is water

number = int(input("Enter the number to check: "))

if number % 5 == 0 and number % 6 == 0 and number % 7 == 0:
    print("light, fire, and water")
elif number % 5 == 0 and number % 6 == 0:
    print("light and fire")
elif number % 5 == 0 and number % 7 == 0:
    print("light and water")
elif number % 6 == 0 and number % 7 == 0:
    print("fire and water")
elif number % 5 == 0:
    print("It is light")
elif number % 6 == 0:
    print("fire")
elif number % 7 == 0:
    print("water")
else:
    print("none")
