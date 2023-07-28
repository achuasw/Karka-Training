#for i in range(1,10):
 #   print(i)

"""number=[1,2,3,4,5]
sum=0
for num in number:
    sum=sum+num
print(sum)"""

"""words=["apple","aswin","mars","female"]
for word in words:
    print("The follwing lines will print each letter of words:",word)
    for letter in word:
        print(letter)"""

"""nums=[1,3,5,7,9]
no=int(input("Enter the number:"))
found=False
for num in nums:
    if no==num:
        found=True
        break
print(f"The number {no} is present,So it is {found}")"""

"""a=[1,4,-8,-4,2,-10]
b=[]
positive=0
for i in a:
    if i<0:
        continue
        
    positive=i
    b.append(positive)
print(b)"""


"""def sum_even_nums(even_num):
    total=0
    for even in even_num:
        if even%2==0:
            total=total+even
           
    print(total)
sum_even_nums([2,3,6,8,10,11,5])"""

lists={"fruits":"apple",
      "vegtable":"potato",
      "name":"aswin",
      "city":"nagercoil",
      "experience":{"years":" 0years",
                    "company_name":"zoho",
                    "skill":"developer"}}


#print(lists["experience"]["years"])
for list in lists:
    print(list,lists[list])
    
