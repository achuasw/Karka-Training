# i=1
# while i<10:
#     i=i+1
#     print(i)

# dictionary={"name":"aswin",
#             "age":18,
#             "mbl":9739202}
# list=list(dictionary.items())
# print(list)

# fib1=0
# fib2=1
# num=int(input("Enter the  number: "))
# for i in range(0,num):
#     if i<=1:
#         next=i
#     else:
#         next=fib1+fib2 #1,2,3,5,8,13....
#         fib1=fib2 #1,1,2,3,5,....
#         fib2=next #1,2,3,5,8,....

#     print(next)


# fact=0
# n=int(input("Enter the number :"))
# for i in range(0,n+1):
#     if i==0:
#         fact=1
#     else:
#         fact=fact*i
#     print(fact)


lst=[3,2,2,3]
new_lst=[]
old_lst=[]
for i in lst:
    if lst[i]!=3:
        new_lst=new_lst+[lst[i]]
   
for j in range(len(lst)+1):
    if j==2:
        old_lst=new_lst
    else:
        old_lst=old_lst+["*"]
print(old_lst)

 
# days=["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]
# total_days=30
# #day_lists=[]
 
# for i in range(len(days)):
#     a=[]
#     for j in range(i+1,total_days+1,len(days)):
#         a=a+[j]
#     week={"day":days[i],"days_list":a}
#     print(week)
#     day_lists.append(week)
# print(day_lists)



# rows=int(input("Enter the rows: "))
# k=1
# for i in range(1,rows+1):
#     for j in range(1,k+1):   
#         print("*",end=" ")
#     k=k+2
#     print()

# rows=int(input("Enter the row value: "))
# for i in range(0,rows):
#     for j in range(0,(rows-i)-1):   
#         print(end=" ")
#     for k in range(0,i+1):
#         print("*",end=" ")
#     print()


# l=[1,5,3,7,9,13]
# for i in range(len(l)):
#     for j in range(i+1,len(l)):
#         if l[i]+l[j]==10:
#             print([i,j])
#     break

# a=0    
# b=1    
# value=int(input("Enter the value : "))
# for i in range(0,value):  
#     print(a)
#     c=a+b
#     a=b 
#     b=c


# a=int(input("Enter the number: "))
# for i in range(0,a):
#     for j in range(0,i+1):
#         print(end=" ")
#     for k in range(0,a-i):
#         print("*",end=" ")
#     print()
      

a=int(input("Enter the number: "))
for i in range(a*a,0,-1):
    # print(i,end=" ")
    if i%a==0:
        print(i)

    else:
        print(i,end=" ")

    
