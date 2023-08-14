# nums=[22,26,22,26,10,9]
# list=[]
# for i in nums:
#     count=0
#     for j in range(len(nums)):
#         if i==nums[j]:
#             count=count+1
# #     if count<=1:
# #         list.append(i)
#     if count==1:
#         print(i)
# print(list)

   
       
# s="abcabbb"
# string=""
# for i in s:
#     if i not in string:
#         string=string+i
# print(string,"with the length of",len(string))



a=["flower","flow","flight"]
string=""
prefix=a[0]
for i in a[1:]:
    while i[:len(prefix)]!=prefix:
        prefix=prefix[:len(prefix)-1]
    if not prefix:
        break
string=prefix

print(string)