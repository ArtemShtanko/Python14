

# while True:
#     number = int(input("Please input number:"))
#     user_choise = input("Y or N")
#     if user_choise == "Y":
#         while True:
#          print(number)
#          number = number - 1
#          if number <= 0:
#             break
#         break
#     if user_choise == "N":
#         break
# print("User choose:", user_choise)

############################################################################

# a = int(input("Input a:"))
# b = int(input("Input b:"))

# test = a + b

# print(test)

############################################################################

# mac_original = input("Input mac address:")


# if "a" in mac_original or "b" in mac_original or "c" in mac_original or "d" in mac_original or "e" in mac_original or "f" in mac_original:


# if "a" not in mac_original or "b" not in mac_original or "c" not in mac_original or "d" not in mac_original or "e" not in mac_original or "f" not in mac_original:

#     print(bool(mac_original))
#     print(type(mac_original))
# else:
#     print("Test finished")

############################################################################

### GPT ###

# is_active = input("Is the user active? ")
# is_admin = input("Is the user administrator? ")
# is_permission = input("Does the user have access? ")

# if is_permission.lower() == 'yes' and is_active.lower() == 'yes':
#     access = True
# elif is_admin.lower() == 'yes':
#     access = True
# else:
#     access = False

############################################################################

# num = int(input("Enter an integer number: "))

# is_even = False if num % 2 else True

# print(is_even)
# # print(bool(is_even))

############################################################################

# num = int(input("Enter the integer (0 to 100): "))
# sum = 0
# interaction_sum = 0

# while num > 0:
#     interaction_sum = interaction_sum + 1
#     sum = interaction_sum + sum
#     num = num - 1
# print(sum)

############################################################################

# for variable in range(5):
#     print(variable)

############################################################################

# first = int(input("Enter the first integer: "))
# second = int(input("Enter the second integer: "))


# if first < second:
#     gcd = first
# else:
#     gcd = second

# while first % gcd or second % gcd:
#     gcd = gcd - 1
#     print(first, second)

############################################################################

# num = int(input("Enter integer (0 for output): "))
# sum = 0
# while num != 0:
#     integer = int(input("Please enter integer:"))
#     for char in range(integer):
#         sum = sum + integer
#         sum = sum + 1

#         # sum = sum + 1
#         # sum = sum + integer

#         # sum = 0 + integer

#     print(sum)
#     num = int(input("Enter integer (0 for output): "))

############################################################################

# while True:
#     num = int(input("Enter integer (0 for output): "))
#     if num == 0:
#         break
#     sum = 0
#     for i in range(num+1):
#         sum = sum + i
#     print(sum)

############################################################################

# num = int(input("Enter integer (0 for output): "))
# sum = 0
# while num != 0:
#     # num = int(input("Enter integer (0 for output): "))
#     for i in range(num+1):
#         sum = sum + i
#     print(sum)
#     num = int(input("Enter integer (0 for output): "))

############################################################################


# try:
    
#     sum = 0
#     while True:
#         num = int(input("Enter integer (0 for output): "))
#         if num == 0:
#             break
#         for i in range(num + 1):
#             sum = sum + i
#         print (sum)

# except ValueError:
#     print("Error")

############################################################################

# if test == int("",16):
#     print("Test is ok")
# else:
#     print ("Not ok")



    #  hex_digits = set(string.hexdigits)

############################################################################

# mac = input("Please input number:")

# # for test in mac:

#     # # if "a" < test < "f" and "0" < test < "9":
#     # if "0" < test < "9":
#     #     print(bool(test))
#     #     # if 0 < test < 9:
#     #         # print("yes")

#     # else:
#     #     print("No")

# if mac < "f" in mac:
#     print("OK")



#     # if ((test < '0' or test > '9') and (test < 'a' or test > 'f')):
#     #     print("yes")
     

############################################################################

mac = input("Please input mac:")
try:
    num = int(mac, 16)
    print("Mac is correct")
except ValueError:
    print("Input correct value")