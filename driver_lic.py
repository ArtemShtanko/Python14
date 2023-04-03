
##########################################################################

# age = input("How old are you? ")
# try:
#     age = int(age)
#     if age >= 18:
#         print("You are adult.")
#     else:
#         print("You are infant")
# except ValueError:
#     print(f"{age} is not a number")

##########################################################################

# age = input("How old are you? ")
# try:
#     age = int(age)
#     if age == int(age):
#         True
# except ValueError:
#     print(f"{age} is not a number")
# print(type(age))

##########################################################################

name = input("Name:")
age = input("Age:")
has_driver_licence = input("Choose Yes or No:")

try:
    age = int(age)
    # if age == int(age):
    #     True

    if name and age >= 18 and has_driver_licence == "Yes":
        print(f"User {name} can rent a car")

### the same result ###
    # if name and age >= 18 and "Yes" in has_driver_licence:
    #     print(f"User {name} can rent a car")

    else:
        print("You cannot rent a car")

except ValueError:
    print(f" \"{age}\" is not a number")

##########################################################################

