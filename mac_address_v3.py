
# mac_original = input("Input mac address:")

# if ":" or "-" in mac_original:
#     mac_original = mac_original.replace(":" or "-", "")

#     if mac_original == mac_original[:12]:
#         add = "-"
#         mac_new = mac_original[0:4] + add + mac_original[4:8] + add + mac_original[8:]
#         mac_new_lower = mac_new.lower()
#         print(mac_new_lower)
#     else:
#         print ("Length of mac address is incorrect")

#########################################################################################


# mac_original = input("Input mac address:")

# if ":" or "-" in mac_original:
#     mac_original = mac_original.replace(":" or "-", "")

#     if True:
#         try:
#             num = int(mac_original, 16)
#         except ValueError:
#             print("Mac address is incorrect")     
    
#         if mac_original == mac_original[:12]:
#             add = "-"
#             mac_new = mac_original[0:4] + add + mac_original[4:8] + add + mac_original[8:]
#             mac_new_lower = mac_new.lower()
#             print(mac_new_lower)
#         else:
#             print ("Length of mac address is incorrect")

#########################################################################################

# mac_original = input("Input mac address:")

# mac_original = mac_original.replace(":" or "-", "")
# mac_original = mac_original.lower()

# if True:
#     try:
#         num = int(mac_original, 16)
#     except ValueError:
#         print("Mac address is incorrect")     

# if mac_original == mac_original[:12]:
#     add = "-"
#     mac_new = mac_original[0:4] + add + mac_original[4:8] + add + mac_original[8:]
#     mac_new_lower = mac_new.lower()
#     print(mac_new_lower)
# else:
#     print ("Length of mac address is incorrect")

#########################################################################################

# mac_original = input("Input mac address:")
# add = "-"
# mac_original = mac_original.replace(":" or "-", "")
# mac_original = mac_original.lower()

# if True:
#     try:
#         num = int(mac_original, 16)
#     except ValueError:
#         print("Mac address is incorrect")
        
# if mac_original == mac_original[:12]:
#     mac_new = mac_original[0:4] + add + mac_original[4:8] + add + mac_original[8:]
#     mac_new_lower = mac_new.lower()
#     print(mac_new_lower)

# else:
#     print ("Length of mac address is incorrect")

#########################################################################################

mac_original = input("Input mac address:")
add = "-"
mac_original = mac_original.replace(":" or "-", "")
mac_original = mac_original.lower()

try:

    num = int(mac_original, 16)

    if mac_original == mac_original[:12] and num:
        mac_new = mac_original[0:4] + add + mac_original[4:8] + add + mac_original[8:]
        mac_new_lower = mac_new.lower()
        print(mac_new_lower)

    else:
        print ("Length of mac address is incorrect")

except ValueError:
    print("Mac address is incorrect")
