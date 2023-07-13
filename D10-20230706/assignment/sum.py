"""numbers=[75,85,95,25,55]
totl_number=0
enum_numbers=enumerate(numbers)
print(type(enum_numbers))
for i,number in enum_numbers:
    print("Entering iteration process of item:"+str(i))
    print("before process",totl_number)
    totl_number=totl_number+number
    print("after process",totl_number)
    print("Exiting iteration process of item:"+str(i))
    print("\n")
print("total number=",totl_number)
average=totl_number/len(numbers)
print(average)"""


costs=[500,200,700,1000]
currency=[]
code="INR "
enum_costs=enumerate(costs)
for i,cost in enum_costs:
    print("Entering iteration process of item:"+str(i))
    print("before process:",cost)
    print("after process:",code+str(cost))
    currency.append(code+str(cost))
    #print(currency)
    print("\n")
print("Output:",currency)    
    


   









   

    
    


     
     
    
    

    
        

