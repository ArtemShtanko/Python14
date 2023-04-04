

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

mac_original = input("Input mac address:")


if "a" in mac_original or "b" in mac_original or "c" in mac_original or "d" in mac_original or "e" in mac_original or "f" in mac_original:


# if "a" not in mac_original or "b" not in mac_original or "c" not in mac_original or "d" not in mac_original or "e" not in mac_original or "f" not in mac_original:

    print(bool(mac_original))
    print(type(mac_original))
else:
    print("Test finished")



