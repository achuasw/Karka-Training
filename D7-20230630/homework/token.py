"""item1=int(input("Enter the amount of item1="))
item2=int(input("Enter the amount of item2="))
item3=int(input("Enter the amount of item3="))
item4=int(input("Enter the amount of item4="))
total=item1+item2+item3+item4
print("Total=",total)
if (total>=500)and(total<=1000):
    print("You have owned a silver token")
else:
    print("You have owned a golden token")"""


item1=int(input("Enter the amount of item1="))
item2=int(input("Enter the amount of item2="))
item3=int(input("Enter the amount of item3="))
item4=int(input("Enter the amount of item4="))
total=item1+item2+item3+item4
print("Total=",total)
if (total>=500)and(total<=1000):
    print("You have owned a silver token")
elif(total<500):
    print("you have not purchased enough to buy a tokens")
else:
    print("You have owned a golden token")
