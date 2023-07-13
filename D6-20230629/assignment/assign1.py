"""num=2
print(num-1,num,num+1,"#")
print(num-1,num,"#",num+1)
print(num-1,"#",num,num+1)
print("#",num-1,num,num+1)"""

#leap year
year=int(input("Enter the year:"))
if year%4==0 and year!=100 or year%400==0:
    print(year,"is a leap year")
else:
    print(year,"is not a leap year")