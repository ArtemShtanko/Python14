
message = input("Введите сообщение: ")
offset = int(input("Введите сдвиг: "))
encoded_message = ""
for ch in message:
    if 122 >= ord(ch) >= 97:
        pos = ord(ch) - ord("a")
        pos = (pos + offset) % 26
        encoded_message = encoded_message + chr(pos + ord("a"))
        # print(encoded_message)
    elif 90 >= ord(ch) >= 65:
        pos = ord(ch) - ord("A")
        pos = (pos + offset) % 26
        encoded_message = encoded_message + chr(pos + ord("A"))
        # print(encoded_message)

    # elif 64 >= ord(ch) >= 32:
    #     encoded_message = ch

    else:
        encoded_message = encoded_message + ch
         
print(encoded_message)

