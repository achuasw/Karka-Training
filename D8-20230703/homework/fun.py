def arithmetic_operations(num1,operator,num2):
    if operator=="+":
        return num1+num2
    elif operator=="-":
        return num1-num2
    elif operator=="*":
        print("mul")
        return num1*num2
    elif operator=="/":
        return num1/num2
    elif operator=="**":
        return num1**num2
    elif operator=="%":
        return num1%num2
    else:
        return "wrong operator"

number1=int(input("Enter the first number="))
oper=(input("Enter the operator="))
number2=int(input("Enter the second number="))
operations=arithmetic_operations(number1,oper,number2)
print(operations)

"""def arithmetic_operations(num1,operator,num2):
    if operator=="+":
        return num1+num2
    else:
        return "wrong operator"
num1=int(input("Enter the first number= "))
operator=(input("Enter the operator=" ))
num2=int(input("Enter the second number= "))
operations=arithmetic_operations(num1,operator,num2)
print(operations)"""



    