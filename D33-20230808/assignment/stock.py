# a=[100,180,260,310,40,535,695]
# profit=a[0]
# for i in range(len(a)):
#     for j in range(1,len(a)):
#         diff=a[j]-a[i]
#         if diff>profit:
#             profit=diff
#             n1=i
#             n2=j
            
# print(profit,(n1,n2))

n=int(input("Enter the days: "))
i=0
amt=[]
profit=0
while i<n:
    amount=int(input("Enter the list of amounts: "))
    amt=amt+[amount]
    i=i+1

for i in range(len(amt)):
    for j in range(1,len(amt)):
        diff=amt[j]-amt[i]
        if diff>profit:
            profit=diff
            n1=i
            n2=j
print(f"The product bought on day {n1}\nThe product sold on day {n2}\nprofit is: {profit}")


# nums=[[1,2],[3,4],[22,10]]
# operations=input("Enter the operator: ")
# a=0
# b=0
# list=[]

# for i in nums:
#     for j in range(len(i)):
#         if operations=="add":
#             a=a+i[j]
#         elif operations=="string":
#             list=list+[i[j]]
#         elif operations=="sub":
#             b=i[j]-b
# if operations=="add":
#     print(a)
# elif operations=="sub":
#     print(b)
# elif operations=="string":
#     print(str(list))


num=int(input("Enter the number: "))
count=0
if num>=1:

    for i in range(1,num+1):
        if num%i==0:
            count=count+1
    if count<=2:print("o")  
    else:print("i")