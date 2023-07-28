# def add(a,b):
#     c=a+b
#     return c
# num1=int(input("Enter the number: "))
# num2=int(input("Enter the number: "))
# d=add(num1,num2)
# print(d)

# def sub(var1,var2,var3):
#     minus=var1-(var2*var3)
#     return minus
# a1=int(input("Enter the number: "))
# a2=int(input("Enter the number: "))
# e=sub(a1,a2,d)
# print(e)


i=0
b=[]
while i<10:
   
    
    candidate=input("Enter the name: ")
    
    if candidate=="A"or candidate=="B" or candidate=="C":
        b.append(candidate)
        i=i+1
    else:
        print("error")

c=b.count("A")

d={"candidate A ",c}

# b["candidate A"]=c
# print(b)


    

    

