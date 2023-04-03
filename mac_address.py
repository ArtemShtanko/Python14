
mac_original = input("Input mac address:")

# if "1,2,3,4,5,6,7,8,9,0" not in mac_original:
#     print ("Mac address is incorrect")


# if int(mac_original, 16) not in mac_original:
#     print ("Mac address is incorrect")


if mac_original > mac_original[:18]:
    print ("Mac address is incorrect")

elif mac_original.range(0, 9999) not in mac_original:
    print ("Mac address is incorrect")

elif ":" in mac_original:
    mac_original_1 = mac_original.replace(":", "")
    # add = "-"[:3]
    add = "-"
    mac_original_2 = mac_original_1[0:4] + add + mac_original_1[4:8] + add + mac_original_1 [8:]
    mac_original_2_lower = mac_original_2.lower()
    print(mac_original_2_lower)

elif "-" in mac_original:
    mac_original_1 = mac_original.replace("-", "")
    # add = "-"[:3]
    add = "-"
    mac_original_2 = mac_original_1[0:4] + add + mac_original_1[4:8] + add + mac_original_1 [8:]
    mac_original_2_lower = mac_original_2.lower()
    print(mac_original_2_lower)