# result = None
# operand = None
# operator = None
# wait_for_number = True

# while True:
#     if wait_for_number:
#         try:
#             operand = float(input("Input number:"))
#             wait_for_number = False
#         except ValueError:
#             print(f"{operand} is not a number")
#             continue
#     else:
#         while not wait_for_number:
#             operator = input("Input +, -, *, / or = to finish:")
#             if operator not in {"=", "+", "-", "*", "/"}:
#                 print (f"{operator} input + or - or * or / or =.")
#                 wait_for_number = False
#                 continue
#             wait_for_number = True

#         if not result:
#             result = operand
#         if operator:
#             if operator == "=":
#                 print(f"Result:{result}")
#                 break
#             elif operator == "+":
#                 result = result + operand
#             elif operator == "-":
#                 result = result - operand
#             elif operator == "*":
#                 result = result * operand
#             elif operator == "/":
#                 result = result / operand

#################################################################################################

result = None
operand = None
operator = None
wait_for_number = True

while True:
    if wait_for_number:
        try:
            operand = float(input("Input number:"))
            wait_for_number = False
        except ValueError:
            print(f"{operand} is not a number")
            continue
    else:
        while not wait_for_number:
            operator = input("Input +, -, *, / or = to finish:")
            if operator not in {"=", "+", "-", "*", "/"}:
                print (f"{operator} input + or - or * or / or =.")
                wait_for_number = False
                continue
            wait_for_number = True

        if not result:
            result = operand
        if operator:
            if operator == "=":
                print(f"Result:{result}")
                break
            elif operator == "+":
                result = result + operand
            elif operator == "-":
                result = result - operand
            elif operator == "*":
                result = result * operand
            elif operator == "/":
                result = result / operand