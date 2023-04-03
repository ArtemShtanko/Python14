
# mac_original = input("Input mac address:")

# # print(len(mac_original))

# if mac_original > mac_original[:17]:
#     print ("Mac address is incorrect")

# elif ":" or "-" in mac_original:
#     mac_original_1 = mac_original.replace(":" or "-", "")
#     add = "-"
#     mac_original_2 = mac_original_1[0:4] + add + mac_original_1[4:8] + add + mac_original_1 [8:]
#     mac_original_2_lower = mac_original_2.lower()
#     print(mac_original_2_lower)

# else:
#     print ("Finished")


#################################################################################################################


mac_original = input("Input mac address:")

# print(len(mac_original))

# if mac_original > mac_original[:17]:
#     print ("Mac address is incorrect")

if ":" or "-" in mac_original:
    mac_original = mac_original.replace(":" or "-", "")
    if mac_original == mac_original[:12]:
        add = "-"
        mac_original_2 = mac_original[0:4] + add + mac_original[4:8] + add + mac_original[8:]
        mac_original_2_lower = mac_original_2.lower()
        print(mac_original_2_lower)
    else:
        print ("Enter correct value")


#################################################################################################################


# mac_original = input("Input mac address:")

# if str("a") or "b" or "c" or "d" or "e" or "f" not in mac_original:
#     print(bool(mac_original))
#     print(type(mac_original))
# #     print ("Error_1")

# #     if ":" or "-" in mac_original:
# #         mac_original = mac_original.replace(":" or "-", "")

# #         if mac_original == mac_original[:12]:
# #             add = "-"
# #             mac_original_2 = mac_original[0:4] + add + mac_original[4:8] + add + mac_original[8:]
# #             mac_original_2_lower = mac_original_2.lower()
# #             print(mac_original_2_lower)
# # else:
# #     print ("Enter correct value")