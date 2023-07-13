#numbers=[1,100,300,4]
#number=max(numbers)
#print("greatest number:",number)

"""numbers=[2,100,300,4]
for i,number in enumerate(numbers):
    check=number>i
    print(check)"""
    

"""numbers=[1,100,300,4]
largest_number=numbers[0]
for i in numbers:
    if i>largest_number:
        largest_number=i
    else:
        print(i,"is smaller")
print(largest_number)        """

lists=[1,100,1100,4,4000,5000,1000]
def largest_number():
    bigger=lists[0]
    for i in lists:
        if i>bigger:
            bigger=i
    return bigger
big=largest_number()
print("largest number:",big)





   
    
            
