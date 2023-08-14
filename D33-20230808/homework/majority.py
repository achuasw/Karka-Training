num=[5,6,7,3,7,5,7,0,9,3,7,9,5,7,9,7,7,4,6,0,8,9,9,6,9,9,9]
total=0
for i in range(len(num)):
    count=0
    for j in range(len(num)):
        if num[i]==num[j]:
            count=count+1 
               
        if count>total:
            total=count
            majority=num[i]
            
print(majority,"is a majority element")
        