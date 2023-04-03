
mac_original = input("Input mac address:")


# if mac_original > mac_original[:17]:     ### does not work
#     print ("Mac address is incorrect")

if ":" in mac_original:
    mac_original_1 = mac_original.replace(":", "")

elif "-" in mac_original:
    mac_original_1 = mac_original.replace("-", "")


add = "-"
mac_original_2 = mac_original_1[0:4] + add + mac_original_1[4:8] + add + mac_original_1 [8:]
mac_original_2_lower = mac_original_2.lower()
print(mac_original_2_lower)
