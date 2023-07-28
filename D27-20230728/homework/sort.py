# a=[-5,-23,5,0,23,-6,23,67]
# b=[]
# c=a[0]
# for i in a:
#     if i<c:
#         c=i
#         b=b+[i]

#     print(b)


a=[1,0,2,0,3,0,4,0,5,0]
b=[]
new=[]
for i in a:
    b=b+[i]
    if i==0:
        b=b+[i+0]
        for j in len(a):
            new=new+[i]

print(len(new))