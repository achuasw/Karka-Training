# a=int(input("Enter the number: "))
# for i in range(0,a):
#     #print(i)
#     #print(i*"*")
#     #print(a*"*")
#     #print("* * * * *")
#     for j in range(a):
#         print("*",end=" ")
#     print("")
        

b=int(input("Enter the number: "))
# num=0
# for i in range(1,b*b+1):
#     #print(i)
#     print(i,end=" ")
#     if i%b==0:
#         #print(i,end=" ")
#         print("")


    
for j in range(b):
    #print(j)
    for i in (range((b*b),0,-1)):  
        if i%b==0:
            #print(i)
            print("")
    print(i,end=" ")
       