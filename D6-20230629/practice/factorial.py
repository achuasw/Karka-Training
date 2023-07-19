"""def factorial(no):
    if no==0 or no==1:
        return 1
    else:
        return no*factorial(no-1)
#num=int(input("Enter the number: "))
fact=factorial(9)
print(fact)"""

num=10
factorial=0
for i in range(1,num+1):
    factorial=factorial+i
    print(factorial)


