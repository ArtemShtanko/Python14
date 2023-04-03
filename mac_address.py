
mac_original = input("Input mac address:")

# print(len(mac_original))

if mac_original > mac_original[:17]:
    print ("Mac address is incorrect")

elif ":" in mac_original:
    mac_original_1 = mac_original.replace(":", "")
    add = "-"
    mac_original_2 = mac_original_1[0:4] + add + mac_original_1[4:8] + add + mac_original_1 [8:]
    mac_original_2_lower = mac_original_2.lower()
    print(mac_original_2_lower)

elif "-" in mac_original:
    mac_original_1 = mac_original.replace("-", "")
    add = "-"
    mac_original_2 = mac_original_1[0:4] + add + mac_original_1[4:8] + add + mac_original_1 [8:]
    mac_original_2_lower = mac_original_2.lower()
    print(mac_original_2_lower)