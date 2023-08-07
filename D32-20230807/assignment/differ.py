num=[2,5,8,1,9,3,7]
absolute=0
diffr=0
c,d=0,0
for i in range(len(num)):
    for j in range(i+1,len(num)):
        minus=num[i]-num[j]
        absolute=abs(minus)
        if absolute>diffr:
            diffr=absolute
            c,d=num[i],num[j]
            

print(diffr,(c,d))