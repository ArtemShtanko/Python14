
print("Enter values") 

math = a,z,b = int(input()), input(), int(input())


if "+" in math:
    print ("Answer:",a,"+",b,"=",a+b)

elif "**" in math:   # ** Піднесення до степеня 
        print ("Answer:", a**b)

elif "*" in math:
        print ("Answer:", a*b)

elif "-" in math:
    if a < b:
        print ("First value is incorrect")
    if a > b:
        print ("Answer:", a-b)

elif "/" in math:
    if a < b:
        print ("First value is incorrect")
    answer = a/b
    if a > b and answer == int(answer):                             
        print ("Answer:", int(answer))          
    if answer != int(answer):
        print ("end")

elif "+" or "-" or "*" or "**" or "/" not in math:
    print ("Please, enter correct value")
