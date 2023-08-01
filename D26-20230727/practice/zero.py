zero=[1,0,2,0,3,4,5,0]
num=[]
final=[]
for i in zero:
    num=num+[i]
    if i==0:
        num=num+[i]
print(num)
for j in range(len(zero)):
    final=final+[num[j]]

print(final)



# a=[3,2,2,3]
# b=[]
# for i in a:
#     if i==3:
#         b=b+["*"]
#     else:
#         b=b+[i]
# print(b)

# a="level"
# b=" "
# for i in a:
#     b=b+i
# if a==i:
#     print(True)
# else:
#     print(False)

# i=0
# b=[]
# while i<11:
#     i=i+1
#     candidate=(input("Enter the number: "))
#     if candidate=="A":
#         b.append(candidate)
        
# print(b)

