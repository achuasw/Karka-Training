num1=int(input("Enter the number one: "))
num2=int(input("Enter the number two: "))
num3=int(input("Enter the number three: "))


if num1>num2:
    if num1>num3:
        print(num1,"is bigger number")
    else:
        print(num3,"is bigger number")
elif num2>num1:
    if num2>num3:
        print(num2,"is bigger number")
    else:
        print(num3,"is bigger number")
elif num3>num1:
    if num3>num2:
        print(num3,"is bigger number")
    else:
        print(num2,"is bigger")


if num3>num1:
    if num3>num2:
        print(num3,"bigger")
    else:
      print(num2,"bigger")    
elif num2>num1:
    print(num2,"is bigger")
else:
    print(num1,"is bigger")


a=-20
b=30
c=10
d=0

if a<d:
    d=a
elif b<d:
    d=b
elif d<c:
    d=c
print(d)

