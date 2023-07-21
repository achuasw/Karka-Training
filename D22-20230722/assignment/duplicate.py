dup_val=[1,2,3,2,5,1,5]
new_list=[]
for i in dup_val:
    print(i)
    if i not in new_list:
        new_list.append(dup_val)
print(new_list)