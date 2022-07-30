#Calculator
#Programmer : Phone Myat Thura Kyaw
#Date : 2022/07/03
while 1:
    fNumber = int(input("Enter First Number"))
    operator = input("Enter Operator")
    sNumber = int(input("Enter Second Number"))
    if operator == "+":
        print('Result is :',fNumber+sNumber)
    elif operator == "-":
        print('Result is :',fNumber-sNumber)
    elif operator == "*":
        print('Result is :',fNumber*sNumber)
    elif operator == "/":
        print('Result is :',fNumber/sNumber)
    else :
        print("Your Operator is wrong")
    


