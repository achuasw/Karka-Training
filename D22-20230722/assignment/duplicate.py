# dup_val=[1,2,3,2,5,1,5]
# new_list=[]
# for i in dup_val:
#     if i not in new_list:
#         new_list=new_list+[i]
# print(new_list)

def addition(a,b):
    c=a+b
    return c
num1=int(input("Enter the number:"))
num2=int(input("Enter the number: "))
total=addition(num1,num2)
print(total)