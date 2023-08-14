# nested_list=[ [ 1, 2, 3, [ 4, 5 ] ], [6, 7, [8, 9] ], [ 10, [ 11,12,13 ] ] ]
# def print_nested_list(nested_list):
#     new_list=[]
#     for i in nested_list:
#         if isinstance(i, list):
#             new_list.extend(print_nested_list(i))
#         else: 
#             new_list.append(i) 
#     return new_list 

# single_list=print_nested_list(nested_list) 
# print(single_list)

# lists=[[1,2,3,[4,5]],[6,7,[8,9]],[10,[11,12,13]]]
# def print_nested_list(lists):
#     for i in lists:
#         if type(i)==list:
#             print_nested_list(i)
#         else:
#             print(i,end=" ")
# print_nested_list(lists)

x=int(input("E3nter the size of list:"))
y= int(input("Enter the size of sublist:"))
list1=[]
sublist=[]
for i in range(x):
    for j in range(y):
        sublist.append(input())
    list1.append(sublist)
    sublist=[]
print (list1)