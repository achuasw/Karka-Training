num=[22,6,10,5,9,7,11]
greater_num=num[0]
smaller_num=num[0]
for i in range(1,len(num)):
    if num[i]>greater_num:
        greater_num=num[i]
    elif num[i]<smaller_num:
        smaller_num=num[i]
print(f"The maximum element is: {greater_num}\nThe minimum element is: {smaller_num}")